import pymysql
import pandas as pd
from pyomo.environ import *
from pyomo.opt import SolverFactory
import os


# Establish a secure connection to the MySQL database using pymysql
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='root',  # Replace with actual password or environment variable
    port=3307,  # Adjust if necessary
    database='mflg'
)

print("DB connected successfully!")

query = "SELECT * FROM table_name"
cursor = connection.cursor()

cursor.execute("SELECT * FROM Wage")
results = cursor.fetchall()

for row in results:
  print(row)

cursor.execute("SELECT * FROM Employees")
results2 = cursor.fetchall()
for row in results2:
  print(row)

cursor.execute("SELECT * FROM Availability")
results3 = cursor.fetchall()
for row in results3:
    print(row)

availability = {} # dictionary to store availability data for the coming week.


df = pd.DataFrame(results2, columns = ['id', 'first_name', 'last_name', 'age', 'email', ' gender', 'primary_role', 'secondary_role', 'wage', 'status', 'address'])
print(df)

workers = df['id'].tolist()
# Staff needs per Day
# change inputs to demand forecast
n_staff = [6, 6, 6, 6, 7, 7, 7]
n_staff_server = [2, 2, 2, 2, 2, 2, 2]
n_staff_cook =  [2, 2, 2, 2, 2, 2, 2]
n_staff_dishwasher = [2, 2, 2, 2, 3, 3, 3]
n_staff_manager = [1, 1, 1, 1, 1, 1, 1]
# Define days (1 week)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

staff_per_day = {day: n_staff[days.index(day)] for day in days}
server_per_day = {day: n_staff_server[days.index(day)] for day in days}
cook_per_day = {day: n_staff_cook[days.index(day)] for day in days}
dishwasher_per_day = {day: n_staff_dishwasher[days.index(day)] for day in days}

# Enter shifts of each day
shifts = ['morning', 'night', 'full']  
days_shifts = {day: shifts for day in days}  # dict with day as key and list of its shifts as value
shift_duration = {'morning': 8, 
                  'night': 8,
                  'full': 12}  # dict with shift as key and its duration in hours as value
# Cook run on different shifts
cook_shift_duration = {'morning': 10, 
                       'night': 10,
                       'full': 14}  # dict with shift as key and its duration in hours as value
pt_ph_wage = 15 # so can edit
pt_salary = {'Mon' : 13, 
           'Tue' : 13, 
           'Wed' : 13, 
           'Thu' : 13, 
           'Fri' : 14, 
           'Sat' : 14, 
           'Sun' : 14
}

cook_ph_wage = 16
cook_pt_salary = {'Mon' : 14, 
           'Tue' : 14, 
           'Wed' : 14, 
           'Thu' : 14, 
           'Fri' : 15, 
           'Sat' : 15, 
           'Sun' : 15
}

roles = ['Cook', 'Dishwasher', 'Manager', 'Server']

def pt_wage(day,shift, boo = False): #boo if Public Holiday
    duration = shift_duration[shift]
    if boo:
        return pt_ph_wage * duration
    return pt_salary[day] * duration

def cook_pt_wage(day,shift, boo = False): #boo if Public Holiday
    duration = cook_shift_duration[shift]
    if boo:
        return cook_ph_wage * duration
    return cook_pt_salary[day] * duration

def get_status(worker_id):
    status = df[df['id'] == worker_id]['status'].iloc[0]
    return status == 'Full time'

def get_wage(worker_id,day,shift):
    cost = 0
    if not get_status(worker_id):
        if get_role(worker_id) == 'Cook':
            cost = cook_pt_wage(day,shift)
        cost = pt_wage(day,shift)
    return cost

def get_role(worker_id):
    return df[df['id'] == worker_id]['primary_role'].iloc[0]

def get_sec_role(worker_id):
    return df[df['id'] == worker_id]['secondary_role'].iloc[0]
    

workers = df['id'].tolist()  # 10 workers available, more than needed
ft_workers = [worker for worker in workers if get_status(worker)]
pt_workers = [worker for worker in workers if not get_status(worker)]
cooks = [worker for worker in workers if get_role(worker) == 'Cook' ]
servers = [worker for worker in workers if get_role(worker) == 'Server']
dishwashers = [worker for worker in workers if get_role(worker) == 'Dishwasher']
managers = [worker for worker in workers if get_role(worker) == 'Manager']

model = ConcreteModel()
model.DAYS = Set(initialize=days)
model.SHIFTS = Set(initialize=shifts)
model.WORKERS = Set(initialize=workers)
model.PTWORKERS = Set(initialize=pt_workers)
model.FTWORKERS = Set(initialize=ft_workers)
model.COOKS = Set(initialize=cooks)
model.SERVERS = Set(initialize=servers)
model.DISHWASHERS = Set(initialize=dishwashers)
model.MANAGERS = Set(initialize=managers)

availability = {(worker, day, shift): 1 for worker in workers for day in days for shift in shifts} # Remove later
# Set availability to 1 for all workers on all days and shifts initially

# read in availability data

# Define decision variables (assigning workers to shifts)
model.assignment = Var(model.WORKERS, model.DAYS, model.SHIFTS, domain = Binary, initialize = 0)

model.cost = Objective(
    expr=sum(get_wage(worker,day,shift) * model.assignment[worker, day, shift]
             for worker in workers for day in days for shift in shifts),
    sense=minimize
)

model.constraints = ConstraintList()
def availability_constraint(model, worker, day, shift):
    return model.assignment[worker, day, shift] <= availability[worker, day, shift]


model.availability_constraint = Constraint(
    model.WORKERS, model.DAYS,model.SHIFTS, rule=availability_constraint
)

def one_shift_per_day_constraint_rule(model, worker, day):
    return sum(model.assignment[worker, day, shift] for shift in shifts) <= 1   

model.one_shift_per_day_constraint = Constraint(
    model.WORKERS, model.DAYS, rule=one_shift_per_day_constraint_rule
)


def server_shift_constraint_rule(model, day):
    # Calculate the total number of assigned workers for morning and night shifts
    total_assigned_workers_morning = sum(model.assignment[worker, day, s] for worker in model.SERVERS for s in ['morning','full'])
    required_workers_count = server_per_day[day]  # Get the required number of workers for the shift

    return total_assigned_workers_morning == required_workers_count     

def server_shift_constraint_rule_night(model, day):
    # Calculate the total number of assigned workers for morning and night shifts
    total_assigned_workers_morning = sum(model.assignment[worker, day, s] for worker in model.SERVERS for s in ['night','full'])
    required_workers_count = server_per_day[day]  # Get the required number of workers for the shift

    return total_assigned_workers_morning == required_workers_count 

model.server_shift_constraint = Constraint(
    model.DAYS, rule=server_shift_constraint_rule
)

model.server_shift_constraint_night = Constraint(
    model.DAYS, rule=server_shift_constraint_rule_night
)

def cook_shift_constraint_rule(model, day):
    # Calculate the total number of assigned workers for morning and night shifts
    total_assigned_workers_morning = sum(model.assignment[worker, day, s] for worker in model.COOKS for s in ['morning','full'])
    required_workers_count = cook_per_day[day]  # Get the required number of workers for the shift

    return total_assigned_workers_morning == required_workers_count

def cook_shift_constraint_rule_night(model, day):
    # Calculate the total number of assigned workers for morning and night shifts
    total_assigned_workers_morning = sum(model.assignment[worker, day, s] for worker in model.COOKS for s in ['night','full'])
    required_workers_count = cook_per_day[day]  # Get the required number of workers for the shift

    return total_assigned_workers_morning == required_workers_count

model.cook_shift_constraint = Constraint(
    model.DAYS, rule=cook_shift_constraint_rule
)

model.cook_shift_constraint_night = Constraint(
    model.DAYS, rule=cook_shift_constraint_rule_night
)

def dishwasher_shift_constraint_rule(model, day):
    # Calculate the total number of assigned workers for morning and night shifts
    total_assigned_workers_morning = sum(model.assignment[worker, day, s] for worker in model.DISHWASHERS for s in ['morning','full'])
    required_workers_count = dishwasher_per_day[day]  # Get the required number of workers for the shift

    return total_assigned_workers_morning == required_workers_count

def dishwasher_shift_constraint_rule_night(model, day):
    # Calculate the total number of assigned workers for morning and night shifts
    total_assigned_workers_morning = sum(model.assignment[worker, day, s] for worker in model.DISHWASHERS for s in ['night','full'])
    required_workers_count = dishwasher_per_day[day]  # Get the required number of workers for the shift

    return total_assigned_workers_morning == required_workers_count

model.dishwasher_shift_constraint = Constraint(
    model.DAYS, rule=dishwasher_shift_constraint_rule
)

def manager_shift_constraint_rule(model, day):
    # Calculate the total number of assigned workers for morning and night shifts
    total_assigned_workers_morning = sum(model.assignment[worker, day, s] for worker in model.MANAGERS for s in ['morning','full'])
    required_workers_count = 1  # Get the required number of workers for the shift

    return total_assigned_workers_morning == required_workers_count

def manager_shift_constraint_rule_night(model, day):
    # Calculate the total number of assigned workers for morning and night shifts
    total_assigned_workers_morning = sum(model.assignment[worker, day, s] for worker in model.MANAGERS for s in ['night','full'])
    required_workers_count = 1  # Get the required number of workers for the shift

    return total_assigned_workers_morning == required_workers_count

model.manager_shift_constraint = Constraint(
    model.DAYS, rule=manager_shift_constraint_rule
)

model.manager_shift_constraint_night = Constraint(
    model.DAYS, rule=manager_shift_constraint_rule_night
)

model.dishwasher_shift_constraint_night = Constraint(
    model.DAYS, rule=dishwasher_shift_constraint_rule_night
)

def parttime_hours_constraint(model, worker):
    total_hours = sum(model.assignment[worker, day, shift] * shift_duration[shift]
                      for day in model.DAYS for shift in model.SHIFTS)
    return total_hours <= 35
    
model.pt_workers_constraints = Constraint(
    model.PTWORKERS, rule=parttime_hours_constraint
)

def fulltime_hours_constraint(model, worker):
    total_hours = sum(model.assignment[worker, day, shift] * shift_duration[shift]
                      for day in model.DAYS for shift in model.SHIFTS)
    return total_hours <= 44
model.ft_workers_constraints = Constraint(
    model.FTWORKERS, rule=fulltime_hours_constraint
)




model.fulltime_hours_constraint = Constraint(
    model.FTWORKERS, rule=fulltime_hours_constraint
)



# Set NEOS_EMAIL environment variable
os.environ['NEOS_EMAIL'] = 'e0773196@u.nus.edu'
solver = SolverFactory('cbc')  # Select solver
solver_manager = SolverManagerFactory('neos') 

# Solve the model
result = solver_manager.solve(model, opt = solver)

# Print optimized results  
# Change to other format of returning results later
if result.solver.termination_condition == 'optimal':
    print('Optimal solution found:')
    for worker in workers:
        for day in days:
            for shift in shifts:
                if model.assignment[worker, day, shift].value == 1:
                    print(f"Worker {worker} assigned to {shift} shift on {day}.")
    print('Total cost:', model.cost())
else:
    print('No optimal solution found.')