import pymysql
import pandas as pd
import numpy as np
from pulp import *
from demand_forecast import seven_days_demand_forecast
from db_utils import execute_query
from utils import is_holiday, get_global_week, get_avail_data, get_event_data, wage_query, get_employee_data
from datetime import datetime, timedelta


# Establish a secure connection to the MySQL database using pymysql
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='root',  # Replace with actual password or environment variable
    port=3306,  # Adjust if necessary
    database='mflg'
)

 

def staffing_algorithm(ft_hours = 44, pt_hours = 35):
# Define global variables
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    weekend = ['Saturday', 'Sunday']
    global_week = get_global_week()
    df_wage = wage_query()
    df = get_employee_data()

    df_avail = get_avail_data(global_week)
    df_events = get_event_data()

    data = seven_days_demand_forecast().iloc[:, -3:]
    pivot_df = data.pivot_table(index='Time', columns='Day', values='ExpectedCustomers', fill_value=0)
    pivot_df = pivot_df[days]
    pivot_df.index.name = None
    pivot_df.columns.name = None

    def get_status(worker_id):
        status = df[df['emp_id'] == worker_id]['status'].iloc[0]
        return status == 'Full time'

    def get_role(worker_id):
        return df[df['emp_id'] == worker_id]['primary_role'].iloc[0]


    workers = df['emp_id'].tolist()  # 10 workers available, more than needed
    kitchen_workers = [worker for worker in workers if get_role(worker) == 'Kitchen']
    server_workers = [worker for worker in workers if get_role(worker) == 'Service']
    managers = [worker for worker in workers if get_role(worker) == 'Manager']


    # Transpose the DataFrame to have times as rows and days as columns
    hrs = ['1000', '1100', '1200', '1300', '1400', '1500', '1600', '1700', '1800', '1900', '2000', '2100']
    pivot_df.index = hrs


    def get_dates_and_day():
        # Get today's date
        today = datetime.now()
        # Calculate the date of the previous Sunday
        sunday = today - timedelta(days=today.weekday() + 1)
        # Calculate the dates for the current week starting from Sunday
        dates_of_week = [sunday + timedelta(days=i) for i in range(7)]
        return dates_of_week

    dates_of_week = get_dates_and_day()
    dates_of_week = [date_obj.date() for date_obj in dates_of_week]
    dates_of_week = [d.strftime("%Y-%m-%d") for d in dates_of_week]
    ph_week = [is_holiday(date) for date in dates_of_week]
    ph_dict = dict(zip(days, ph_week))
    current_week = pd.DataFrame({"date" : dates_of_week, "day" : days})
    df_events['date'] = pd.to_datetime(df_events['date']).dt.strftime('%Y-%m-%d')
    joined_df = current_week.merge(df_events, on='date', how='inner') # only events that are in the current week
    selected_columns = ['day', 'event_period', 'staffReq']
    extracted_df = joined_df[selected_columns]

    # Array representing shifting hours
    timings = np.array([[1,0,1],
                    [1,1,1],
                    [0,1,1]])   
    # number of shifts
    num_shifts = timings.shape[1]
    # number of time windows
    num_time = timings.shape[0]
    # Define your functions with assumed business rules
    def kitchen_required_func(x):
        if x < 30:
            return 3
        elif x < 70:
            return 4
        else: 
            return 5

    def service_required_func(x):
        if x < 30:
            return 4
        elif x < 70:
            return 5
        else: 
            return 6

    # Map the functions over all entries in the DataFrame and replace them
    df_kitchen_mapped = pivot_df.map(kitchen_required_func)
    df_service_mapped = pivot_df.map(service_required_func)

    time_windows_kitchen = {
        'Morning': df_kitchen_mapped['1000':'1200'].max(),
        'Afternoon' : df_kitchen_mapped['1200':'1800'].max(),
        'Night': df_kitchen_mapped['1800':'2200'].max()
    }


    time_windows_service = {
        'Morning': df_service_mapped['1000':'1200'].max(),
        'Afternoon': df_service_mapped['1200':'1800'].max(),
        'Night': df_service_mapped['1800':'2200'].max()
    }

    for index, row in extracted_df.iterrows():
        period = row['event_period']
        event_day = row['day']
        add_staff = row['staffReq']
        if period == 'Full':
            time_windows_service['Morning'][event_day] += add_staff
            time_windows_service['Afternoon'][event_day] += add_staff
            time_windows_service['Night'][event_day] += add_staff
        else:
            time_windows_service[period][event_day] += add_staff

    df_time_windows_kitchen = pd.DataFrame(time_windows_kitchen)
    df_time_windows_service = pd.DataFrame(time_windows_service)

    shifts = ['Morning', 'Night', 'Full']
    kitchen_staff_dict = {}

    for day in days: 
        temp_lst = list()
        workers_per_shift = LpVariable.dicts("num_workers", shifts, lowBound=0, cat="Integer")

    # Minimize the staff assigned for the aay
        shift_problem = LpProblem("Shift Problem", LpMinimize)

    # Minimize the number of workers
        shift_problem += lpSum(workers_per_shift[i] for i in shifts), "Objective"

        for t in range(num_time):
            shift_problem += lpSum([timings[t, j] * workers_per_shift[shifts[j]]] for j in range(num_shifts)) >= df_time_windows_kitchen.iloc[days.index(day),t]

        for i in shifts:
            shift_problem += workers_per_shift[i] <= df_avail[df_avail['emp_id'].isin(kitchen_workers)][day].to_list().count(i)

        shift_problem.solve(solver = PULP_CBC_CMD(msg=0))

        for shift in shifts:
            temp_lst.append(workers_per_shift[shift].value())
        kitchen_staff_dict[day] = temp_lst

    service_staff_dict = {}

    for day in days: 
        temp_lst = list()
        workers_per_shift = LpVariable.dicts("num_workers", shifts, lowBound=0, cat="Integer")

    # Minimize the staff assigned for the day
        shift_problem = LpProblem("Shift Problem", LpMinimize)

    # Minimize the number of workers
        shift_problem += lpSum(workers_per_shift[i] for i in shifts), "Objective"

        for t in range(num_time):
            shift_problem += lpSum([timings[t, j] * workers_per_shift[shifts[j]] for j in range(num_shifts)]) >= df_time_windows_service.iloc[days.index(day),t]

        for i in shifts:
            shift_problem += workers_per_shift[i] <= df_avail[df_avail['emp_id'].isin(server_workers)][day].to_list().count(shift)

        shift_problem.solve(solver = PULP_CBC_CMD(msg=0))

        for shift in shifts:
            temp_lst.append(workers_per_shift[shift].value())
        service_staff_dict[day] = temp_lst

    print(service_staff_dict)

    service_shift_duration = {1: 8, 
                    2: 8,
                    3: 12}  # dict with shift as key and its duration in hours as value
    # Cook run on different shifts
    kitchen_shift_duration = {1: 10, 
                        2: 10,
                        3: 14}  # dict with shift as key and its duration in hours as value


    def shift_duration(workerid,shiftindex):
        status = get_status(workerid)
        role = get_role(workerid)
        if status: 
            return 0
        else: 
            if role == 'Kitchen':
                return kitchen_shift_duration[shiftindex]
            else:
                return service_shift_duration[shiftindex]
            
    def service_pt_wage(day,shift):
        df_service_wage = df_wage[df_wage['role'] == 'Service']
        duration = service_shift_duration[shift]
        day_type = 'Weekday' if day in weekday else 'Weekend'
        if ph_dict[day]:
            return df_service_wage[df_service_wage['day'] == 'Public Holiday']['wage'].iloc[0] * duration
        return df_service_wage[df_service_wage['day'] == day_type]['wage'].iloc[0] * duration

    def kitchen_pt_wage(day,shift): 
        df_kitchen_wage = df_wage[df_wage['role'] == 'Kitchen']
        duration = kitchen_shift_duration[shift]
        day_type = 'Weekday' if day in weekday else 'Weekend'
        if ph_dict[day]:
            return df_kitchen_wage[df_kitchen_wage['day'] == 'Public Holiday']['wage'].iloc[0] * duration
        return df_kitchen_wage[df_kitchen_wage['day'] == day_type]['wage'].iloc[0] * duration


    def get_wage(worker_id,day,shift):
        cost = 0
        if not get_status(worker_id):
            if get_role(worker_id) == 'Kitchen':
                cost = kitchen_pt_wage(day,shift)
            else:
                cost = service_pt_wage(day,shift)
        return cost

    def get_sec_role(worker_id):
        return df[df['emp_id'] == worker_id]['secondary_role'].iloc[0]

    def get_avail(workerid, day,shifttype):
        try:
            day_value = df_avail.loc[df_avail['emp_id'] == workerid][day].values[0]
            if day_value == 'None':
                return 0
            elif day_value == 'Morning':
                return 1 if shifttype == 1 else 0
            elif day_value == 'Night':
                return 1 if shifttype == 2 else 0
            elif day_value == 'Full':
                return 1
        except:
            print(workerid, day, shifttype)


    def shift_duration(workerid, shift):
        status = get_status(workerid)
        role = get_role(workerid)
        if status: 
            return 0
        else: 
            if role == 'Kitchen':
                return kitchen_shift_duration[shift]
            else:
                return service_shift_duration[shift]
            

    def kitchen_required(day, shift):
        return kitchen_staff_dict[day][shift-1]

    def service_required(day, shift):
        return service_staff_dict[day][shift-1]


    problem = LpProblem("Minimize Staff Costs", LpMinimize)

    morning_shift = LpVariable.dicts('Morning', [(day,worker) for worker in workers for day in days], cat ='Binary')
    night_shift = LpVariable.dicts('Night', [(day,worker) for worker in workers for day in days], cat ='Binary')
    full_shift = LpVariable.dicts('Full', [(day,worker) for worker in workers for day in days],cat ='Binary')

    # Set initial binary values
    for day in days:
        for worker in workers:
            morning_shift[(day, worker)].setInitialValue(0)
            night_shift[(day, worker)].setInitialValue(0)
            full_shift[(day, worker)].setInitialValue(0)

    # Objective function to minimize overall wage
    objective = lpSum(get_wage(worker, day, shift_type) * (
        morning_shift[(day, worker)] if shift_type == 1 else
        night_shift[(day, worker)] if shift_type == 2 else
        full_shift[(day, worker)]
    ) for day in days for worker in workers for shift_type in range(1, 4))


    for day in days:
        for worker in workers:
            problem += lpSum([morning_shift[(day,worker)], night_shift[(day,worker)], full_shift[(day,worker)]]) <= 1  # only one shift per day
            problem += morning_shift[(day,worker)] <= get_avail(worker,day,1) 
            problem += night_shift[(day,worker)] <= get_avail(worker,day,2) 
            problem += full_shift[(day,worker)] <= get_avail(worker,day,3)

    # Define the constraints for total hours worked in a week   
    for worker in workers:
        worker_role = get_role(worker)
        status = get_status(worker)  # pt or ft
        hours_in_a_week = lpSum(
            morning_shift[(day, worker)] * shift_duration(worker, 1) +
            night_shift[(day, worker)] * shift_duration(worker, 2) +
            full_shift[(day, worker)] * shift_duration(worker, 3) for day in days
        )
        problem += hours_in_a_week <= ft_hours if status else hours_in_a_week <= pt_hours  
    
    # One Manager per day
    manager_dict = {}
    for day in days:
        check_full_shift = sum([get_avail(worker,day,3) for worker in managers])
        if check_full_shift  == 0:
            manager_dict[day] = 0
        else:
            manager_dict[day] = 1
    for day in days:
        if manager_dict[day] == 1:
            problem += lpSum([full_shift[(day, worker)] for worker in managers]) == 1
        else:
            problem += lpSum([morning_shift[(day, worker)] + night_shift[(day, worker)] for worker in managers]) == 2
        
    # Define the constraint that each day and shift has optimised number of workers
    for day in days:
        for shift_type in range(1,4):
            if shift_type == 1:
                shift_var = morning_shift
            elif shift_type == 2:
                shift_var = night_shift
            else:
                shift_var = full_shift
            problem += lpSum(shift_var[(day, worker)] for worker in kitchen_workers) == kitchen_required(day,shift_type)
            problem += lpSum(shift_var[(day, worker)] for worker in server_workers) == service_required(day,shift_type)   


    problem.solve(solver = PULP_CBC_CMD(msg=0))
    status = LpStatus[problem.status]

    # Insert into Schema DB
    for day in days:
        for worker in kitchen_workers:
            if morning_shift[(day, worker)].varValue == 1:
                query = f"INSERT INTO Schedules (emp_id, week,day, shift,role) VALUES ({worker},'{global_week}','{day}','Morning', 'Kitchen')"
                execute_query(query)
            elif night_shift[(day, worker)].varValue == 1:
                query = f"INSERT INTO Schedules (emp_id, week,day, shift,role) VALUES ({worker},'{global_week}','{day}','Night', 'Kitchen')"
                execute_query(query)    
            elif full_shift[(day, worker)].varValue == 1:
                query = f"INSERT INTO Schedules (emp_id, week,day, shift,role) VALUES ({worker},'{global_week}','{day}','Full', 'Kitchen')"
                execute_query(query)
        for worker in server_workers:
            if morning_shift[(day, worker)].varValue == 1:
                query = f"INSERT INTO Schedules (emp_id, week,day, shift,role) VALUES ({worker},'{global_week}','{day}','Morning', 'Service')"
                execute_query(query)
            elif night_shift[(day, worker)].varValue == 1:
                query = f"INSERT INTO Schedules (emp_id, week,day, shift,role) VALUES ({worker},'{global_week}','{day}','Night', 'Service')"
                execute_query(query)
            elif full_shift[(day, worker)].varValue == 1:
                query = f"INSERT INTO Schedules (emp_id, week,day, shift,role) VALUES ({worker},'{global_week}','{day}','Full', 'Service')"
                execute_query(query)
        for worker in managers:
            if morning_shift[(day, worker)].varValue == 1:
                query = f"INSERT INTO Schedules (emp_id, week,day, shift,role) VALUES ({worker},'{global_week}','{day}','Morning', 'Manager')"
                execute_query(query)
            elif night_shift[(day, worker)].varValue == 1:
                query = f"INSERT INTO Schedules (emp_id, week,day, shift,role) VALUES ({worker},'{global_week}','{day}','Night', 'Manager')"
                execute_query(query)
            elif full_shift[(day, worker)].varValue == 1:
                query = f"INSERT INTO Schedules (emp_id, week,day, shift,role) VALUES ({worker},'{global_week}','{day}','Full', 'Manager')"
                execute_query(query)
    return status

staffing_algorithm()