# Import the execute_query function from db_utils.py
from db_utils import execute_query
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

# Function to create a new employee
def create_employee(data):
    # Extract employee data from the input dictionary
    name = data.get('name')
    primary_role = data.get('role')
    secondary_role = data.get('secondaryRole')
    wage = data.get('wage')
    status = data.get('employmentType')  # Employment status (e.g., full-time, part-time)
    
    query = "SELECT MAX(emp_id) FROM Employees"
    emp_id = execute_query(query)[0]['MAX(emp_id)'] + 1
    
    # Prepare SQL query to insert into Employees table
    insert_employee_query = f"""
        INSERT INTO Employees (emp_id, name primary_role, secondary_role, wage, status)
        VALUES ('{emp_id}', '{name}', '{primary_role}', '{secondary_role}', {wage}, '{status}')
    """
    
    # Execute the insert query to add the employee to Employees table
    a = execute_query(insert_employee_query)

    # Prepare SQL query to insert into Availability table
    insert_availability_query = f"""
        INSERT INTO Availability (emp_id, week, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
        VALUES  ({emp_id}, '2023-12-31', '{data.get('mon')}', '{data.get('tues')}', '{data.get('wed')}', '{data.get('thurs')}', '{data.get('fri')}', '{data.get('sat')}', '{data.get('sun')}')
    """
    a = execute_query(insert_availability_query)

    # Return the emp_id of the newly created employee
    return a

# Function to create employees
def create_employees(employees_data_list):
    query = "SELECT MAX(emp_id) FROM Employees"
    emp_id = execute_query(query)[0]['MAX(emp_id)'] + 1
    
    for data in employees_data_list:
        # Extract employee data from the input dictionary
        name = data.get('name')
        primary_role = data.get('role')
        secondary_role = data.get('secondaryRole')
        wage = data.get('wage')
        status = data.get('employmentType')  # Employment status (e.g., full-time, part-time)
        
        # Prepare SQL query to insert into Employees table
        insert_employee_query = f"""
            INSERT INTO Employees (emp_id, name, primary_role, secondary_role, wage, status)
            VALUES ('{emp_id}', '{name}', '{primary_role}', '{secondary_role}', {wage}, '{status}')
        """
        
        # Execute the insert query to add the employee to Employees table
        a = execute_query(insert_employee_query)
        
        # Prepare SQL query to insert into Availability table
        insert_availability_query = f"""
            INSERT INTO Availability (emp_id, week, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
            VALUES  ({emp_id}, '2023-12-31', '{data.get('mon')}', '{data.get('tues')}', '{data.get('wed')}', '{data.get('thurs')}', '{data.get('fri')}', '{data.get('sat')}', '{data.get('sun')}')
        """
        execute_query(insert_availability_query)
        
        emp_id += 1  # Increment emp_id for the next employee
    return a

# Function to retrieve all employees
def get_all_employees():
    query = """
        SELECT e.emp_id, e.name,
               e.primary_role, e.secondary_role, e.wage, e.status,
               a.week, a.Monday, a.Tuesday, a.Wednesday, a.Thursday, a.Friday, a.Saturday, a.Sunday
        FROM Employees e
        LEFT JOIN Availability a ON e.emp_id = a.emp_id
        WHERE a.week = (
            SELECT MAX(week)
            FROM Availability
            WHERE emp_id = e.emp_id
        )
    """
    # Execute the query using execute_query function and return the result
    result = execute_query(query)
    
    # Process the result to build a list of employees with their availability
    employees = []
    for row in result:
        emp_id = row['emp_id']
        # Build the employee dictionary
        employee = {
            'id': emp_id,
            'name': f"{row['name']}",
            'role': row['primary_role'],
            'secondaryRole' : row['secondary_role'],
            'employmentType' : row['status'],
            'wage': row['wage'],
            'type': row['status'],
            'mon': row['Monday'],
            'tues': row['Tuesday'],
            'wed': row['Wednesday'],
            'thurs': row['Thursday'],
            'fri': row['Friday'],
            'sat': row['Saturday'],
            'sun': row['Sunday']
        }
        employees.append(employee)
    return employees


# Function to update an employee
def update_employee(emp_id, data):
    # Extract employee data from the input dictionary
    name = data.get('name')  # Use get() to safely retrieve data, allowing for optional fields
    primary_role = data.get('role')
    secondary_role = data.get('secondaryRole')
    wage = data.get('wage')
    status = data.get('employmentType')  # Employment status (e.g., full-time, part-time)

    # Prepare SQL query to update Employees table
    update_employee_query = "UPDATE Employees SET "
    update_set_values = []

    # Build the SET clause of the UPDATE query based on provided fields
    if name is not None:
        update_set_values.append(f"name = '{name}'")
    if primary_role is not None:
        update_set_values.append(f"primary_role = '{primary_role}'")
    if secondary_role is not None:
        update_set_values.append(f"secondary_role = '{secondary_role}'")
    if wage is not None:
        update_set_values.append(f"wage = {wage}")
    if status is not None:
        update_set_values.append(f"status = '{status}'")

    # Join the SET values into the UPDATE query
    update_employee_query += ", ".join(update_set_values)
    update_employee_query += f" WHERE emp_id = {emp_id}"

    # Execute the update query to modify the employee's information
    execute_query(update_employee_query)


    update_availability_query = f"""
            UPDATE Availability
            SET Monday = '{data.get('mon')}',
                Tuesday = '{data.get('tues')}',
                Wednesday = '{data.get('wed')}',
                Thursday = '{data.get('thurs')}',
                Friday = '{data.get('fri')}',
                Saturday = '{data.get('sat')}',
                Sunday = '{data.get('sun')}'
            WHERE emp_id = {emp_id}
        """

    execute_query(update_availability_query)



# Function to delete an employee
def delete_employee(emp_id):
    # Delete from Availability table first
    availability_query = f"DELETE FROM Availability WHERE emp_id = {emp_id}"
    execute_query(availability_query)
    
    # Then delete from Employees table
    employee_query = f"DELETE FROM Employees WHERE emp_id = {emp_id}"
    execute_query(employee_query)


#Function to get list of wages cost for for each month between two months (inclusive)
def get_full_time_wages(start_mmyy, end_mmyy):
    # Parse input month-year values (MMYY) to extract month and year
    start_month = int(start_mmyy[:2])
    start_year = int(start_mmyy[2:])
    end_month = int(end_mmyy[:2])
    end_year = int(end_mmyy[2:])
    
    # List to store monthly total sum of wages for full-time employees
    monthly_totals = []
    
    # Iterate over the months in the specified range
    current_month = start_month
    current_year = start_year
    while (current_year < end_year or (current_year == end_year and current_month <= end_month)):
        # SQL query to retrieve total sum of wages for full-time employees with relevant schedules within the current month
        query = f"""
            SELECT e.name, e.wage, s.starttime, s.endtime
            FROM Employees e
            JOIN Schedules s ON e.emp_id = s.emp_id
            WHERE e.status = 'Full Time'
            AND YEAR(s.week) = {current_year}
            AND MONTH(s.week) = {current_month}
        """
        
        # Execute the query to retrieve the total sum of wages for the current month
        result = execute_query(query)

        total_wages  = 0.0
        for row in result:
            wage = float(row['wage'])
            total_wages += wage
        
        # Append the total sum of wages for the current month to the monthly_totals list
        monthly_totals.append(total_wages)
        
        # Move to the next month
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
    
    return monthly_totals


# Function to calculate total wage expenditure for part-time employees for each month between two months (inclusive)
def get_part_time_wages(start_mmyyyy, end_mmyyyy):
    # Parse input month-year values (MMYY) to extract month and year
    start_month = int(start_mmyyyy[:2])
    start_year = int(start_mmyyyy[2:])
    end_month = int(end_mmyyyy[:2])
    end_year = int(end_mmyyyy[2:])
    
    # List to store monthly total wage expenditures
    monthly_expenditures = []
    
    # Iterate over the months in the specified range
    current_month = start_month
    current_year = start_year
    while (current_year < end_year or (current_year == end_year and current_month <= end_month)):
        # SQL query to retrieve part-time employees' wage and hours worked within the current month
        query = f"""
            SELECT e.name, e.wage, s.starttime, s.endtime
            FROM Employees e
            JOIN Schedules s ON e.emp_id = s.emp_id
            WHERE e.status = 'Part Time'
            AND YEAR(s.week) = {current_year}
            AND MONTH(s.week) = {current_month}
        """
        
        # Execute the query to retrieve part-time employees' data for the current month
        result = execute_query(query)
        # Variable to store total wage expenditure for the current month
        total_wage_expenditure = 0.0
        # Process the query result to calculate total wage expenditure for the current month
        for row in result:
            wage = float(row['wage'])
            shift_start = row['starttime']
            shift_end = row['endtime']
            
            # Calculate hours worked in the shift
            hours_worked = (shift_end - shift_start).total_seconds() / 3600.0
            
            # Calculate wage expenditure for the current shift
            shift_wage_expenditure = wage * hours_worked
            
            # Accumulate the shift wage expenditure to total wage expenditure for the current month
            total_wage_expenditure += shift_wage_expenditure
        
        # Append the total wage expenditure for the current month to the monthly_expenditures list
        monthly_expenditures.append(total_wage_expenditure)
        
        # Move to the next month
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
    
    return monthly_expenditures


#Function to get list of wages cost for for each month between two months (inclusive)
def get_full_time_wages_role(start_mmyy, end_mmyy, role):
    # Parse input month-year values (MMYY) to extract month and year
    start_month = int(start_mmyy[:2])
    start_year = int(start_mmyy[2:])
    end_month = int(end_mmyy[:2])
    end_year = int(end_mmyy[2:])
    
    # List to store monthly total sum of wages for full-time employees
    monthly_totals = []
    
    # Iterate over the months in the specified range
    current_month = start_month
    current_year = start_year
    while (current_year < end_year or (current_year == end_year and current_month <= end_month)):
        # SQL query to retrieve total sum of wages for full-time employees with relevant schedules within the current month
        query = f"""
            SELECT e.name, e.wage, s.starttime, s.endtime, s.role
            FROM Employees e
            JOIN Schedules s ON e.emp_id = s.emp_id
            WHERE e.status = 'Full Time'
            AND YEAR(s.week) = {current_year}
            AND MONTH(s.week) = {current_month}
            AND s.role = '{role}'
        """
        
        # Execute the query to retrieve the total sum of wages for the current month
        result = execute_query(query)

        total_wages  = 0.0
        for row in result:
            wage = float(row['wage'])
            total_wages += wage
        
        # Append the total sum of wages for the current month to the monthly_totals list
        monthly_totals.append(total_wages)
        
        # Move to the next month
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
    
    return monthly_totals


# Function to calculate total wage expenditure for part-time employees for each month between two months (inclusive)
def get_part_time_wages_role(start_mmyyyy, end_mmyyyy,role):
    # Parse input month-year values (MMYY) to extract month and year
    start_month = int(start_mmyyyy[:2])
    start_year = int(start_mmyyyy[2:])
    end_month = int(end_mmyyyy[:2])
    end_year = int(end_mmyyyy[2:])
    
    # List to store monthly total wage expenditures
    monthly_expenditures = []
    
    # Iterate over the months in the specified range
    current_month = start_month
    current_year = start_year
    while (current_year < end_year or (current_year == end_year and current_month <= end_month)):
        # SQL query to retrieve part-time employees' wage and hours worked within the current month
        query = f"""
            SELECT e.name, e.wage, s.starttime, s.endtime, s.role
            FROM Employees e
            JOIN Schedules s ON e.emp_id = s.emp_id
            WHERE e.status = 'Part Time'
            AND YEAR(s.week) = {current_year}
            AND MONTH(s.week) = {current_month}
            AND s.role = '{role}'
        """
        
        # Execute the query to retrieve part-time employees' data for the current month
        result = execute_query(query)
        # Variable to store total wage expenditure for the current month
        total_wage_expenditure = 0.0
        # Process the query result to calculate total wage expenditure for the current month
        for row in result:
            wage = float(row['wage'])
            shift_start = row['starttime']
            shift_end = row['endtime']
            
            # Calculate hours worked in the shift
            hours_worked = (shift_end - shift_start).total_seconds() / 3600.0
            
            # Calculate wage expenditure for the current shift
            shift_wage_expenditure = wage * hours_worked
            
            # Accumulate the shift wage expenditure to total wage expenditure for the current month
            total_wage_expenditure += shift_wage_expenditure
        
        # Append the total wage expenditure for the current month to the monthly_expenditures list
        monthly_expenditures.append(total_wage_expenditure)
        
        # Move to the next month
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
    
    return monthly_expenditures