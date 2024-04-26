# Import the execute_query function from db_utils.py
from db_utils import execute_query
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

def create_employee(data):
    """
    Creates a new employee in the database.

    Args:
        data (dict): A dictionary containing employee data including name, primary role, secondary role, wage, and employment type.

    Returns:
        None
    """
    name = data.get('name')
    primary_role = data.get('role')
    secondary_role = data.get('secondaryRole')
    wage = data.get('wage')
    status = data.get('employmentType')
    query = "SELECT MAX(emp_id) FROM Employees"
    emp_id = execute_query(query)[0]['MAX(emp_id)'] + 1
    insert_employee_query = f"""
        INSERT INTO Employees (emp_id, name primary_role, secondary_role, wage, status)
        VALUES ('{emp_id}', '{name}', '{primary_role}', '{secondary_role}', {wage}, '{status}')
    """
    execute_query(insert_employee_query)
    insert_availability_query = f"""
        INSERT INTO Availability (emp_id, week, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
        VALUES  ({emp_id}, '2023-12-31', '{data.get('mon')}', '{data.get('tues')}', '{data.get('wed')}', '{data.get('thurs')}', '{data.get('fri')}', '{data.get('sat')}', '{data.get('sun')}')
    """
    execute_query(insert_availability_query)

def create_employees(employees_data_list):
    """
    Creates multiple employees in the database.

    Args:
        employees_data_list (list): A list of dictionaries containing employee data.

    Returns:
        None
    """
    query = "SELECT MAX(emp_id) FROM Employees"
    emp_id = execute_query(query)[0]['MAX(emp_id)'] + 1
    
    for data in employees_data_list:
        name = data.get('name')
        primary_role = data.get('role')
        secondary_role = data.get('secondaryRole')
        wage = data.get('wage')
        status = data.get('employmentType')  
        insert_employee_query = f"""
            INSERT INTO Employees (emp_id, name, primary_role, secondary_role, wage, status)
            VALUES ('{emp_id}', '{name}', '{primary_role}', '{secondary_role}', {wage}, '{status}')
        """
        execute_query(insert_employee_query)
        
        insert_availability_query = f"""
            INSERT INTO Availability (emp_id, week, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
            VALUES  ({emp_id}, '2023-12-31', '{data.get('mon')}', '{data.get('tues')}', '{data.get('wed')}', '{data.get('thurs')}', '{data.get('fri')}', '{data.get('sat')}', '{data.get('sun')}')
        """
        execute_query(insert_availability_query)
        
        emp_id += 1  


def get_all_employees():
    """
    Retrieves all employees from the database.

    Returns:
        list: A list of dictionaries containing employee details.
    """
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
    result = execute_query(query)
    employees = []
    for row in result:
        emp_id = row['emp_id']
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



def update_employee(emp_id, data):
    """
    Updates an employee's information in the database.

    Args:
        emp_id (int): The ID of the employee to be updated.
        data (dict): A dictionary containing the updated employee data.

    Returns:
        None
    """
    name = data.get('name') 
    primary_role = data.get('role')
    secondary_role = data.get('secondaryRole')
    wage = data.get('wage')
    status = data.get('employmentType')  
    update_employee_query = "UPDATE Employees SET "
    update_set_values = []

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

    update_employee_query += ", ".join(update_set_values)
    update_employee_query += f" WHERE emp_id = {emp_id}"

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

def delete_employee(emp_id):
    """
    Deletes an employee from the database.

    Args:
        emp_id (int): The ID of the employee to be deleted.

    Returns:
        None
    """
    availability_query = f"DELETE FROM Availability WHERE emp_id = {emp_id}"
    execute_query(availability_query)
    employee_query = f"DELETE FROM Employees WHERE emp_id = {emp_id}"
    execute_query(employee_query)

def get_full_time_wages(start_mmyy, end_mmyy):
    """
    Calculates the total wage expenditure for full-time employees for each month between two months (inclusive).

    Args:
        start_mmyy (str): Start month-year in MMYY format.
        end_mmyy (str): End month-year in MMYY format.

    Returns:
        list: A list of total wage expenditures for each month.
    """
    start_month = int(start_mmyy[:2])
    start_year = int(start_mmyy[2:])
    end_month = int(end_mmyy[:2])
    end_year = int(end_mmyy[2:])

    monthly_totals = []

    current_month = start_month
    current_year = start_year
    while (current_year < end_year or (current_year == end_year and current_month <= end_month)):
        query = f"""
            SELECT e.name, e.wage, s.starttime, s.endtime
            FROM Employees e
            JOIN Schedules s ON e.emp_id = s.emp_id
            WHERE e.status = 'Full Time'
            AND YEAR(s.week) = {current_year}
            AND MONTH(s.week) = {current_month}
        """
        result = execute_query(query)

        total_wages  = 0.0
        for row in result:
            wage = float(row['wage'])
            total_wages += wage

        monthly_totals.append(total_wages)
    
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
    
    return monthly_totals

def get_part_time_wages(start_mmyyyy, end_mmyyyy):
    """
    Calculates the total wage expenditure for part-time employees for each month between two months (inclusive).

    Args:
        start_mmyyyy (str): Start month-year in MMYYYY format.
        end_mmyyyy (str): End month-year in MMYYYY format.

    Returns:
        list: A list of total wage expenditures for each month.
    """
    start_month = int(start_mmyyyy[:2])
    start_year = int(start_mmyyyy[2:])
    end_month = int(end_mmyyyy[:2])
    end_year = int(end_mmyyyy[2:])
    monthly_expenditures = []
    current_month = start_month
    current_year = start_year
    while (current_year < end_year or (current_year == end_year and current_month <= end_month)):
        query = f"""
            SELECT e.name, e.wage, s.starttime, s.endtime
            FROM Employees e
            JOIN Schedules s ON e.emp_id = s.emp_id
            WHERE e.status = 'Part Time'
            AND YEAR(s.week) = {current_year}
            AND MONTH(s.week) = {current_month}
        """
        result = execute_query(query)
        total_wage_expenditure = 0.0
        for row in result:
            wage = float(row['wage'])
            shift_start = row['starttime']
            shift_end = row['endtime']
            hours_worked = (shift_end - shift_start).total_seconds() / 3600.0
            shift_wage_expenditure = wage * hours_worked
            total_wage_expenditure += shift_wage_expenditure
        monthly_expenditures.append(total_wage_expenditure)

        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
    
    return monthly_expenditures


def get_full_time_wages_role(start_mmyy, end_mmyy, role):
    """
    Calculates the total wage expenditure for full-time employees of a specific role for each month between two months (inclusive).

    Args:
        start_mmyy (str): Start month-year in MMYY format.
        end_mmyy (str): End month-year in MMYY format.
        role (str): The role of the employees.

    Returns:
        list: A list of total wage expenditures for each month.
    """
    start_month = int(start_mmyy[:2])
    start_year = int(start_mmyy[2:])
    end_month = int(end_mmyy[:2])
    end_year = int(end_mmyy[2:])
    monthly_totals = []
    current_month = start_month
    current_year = start_year
    while (current_year < end_year or (current_year == end_year and current_month <= end_month)):
        query = f"""
            SELECT e.name, e.wage, s.starttime, s.endtime, s.role
            FROM Employees e
            JOIN Schedules s ON e.emp_id = s.emp_id
            WHERE e.status = 'Full Time'
            AND YEAR(s.week) = {current_year}
            AND MONTH(s.week) = {current_month}
            AND s.role = '{role}'
        """
        result = execute_query(query)

        total_wages  = 0.0
        for row in result:
            wage = float(row['wage'])
            total_wages += wage
        monthly_totals.append(total_wages)
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
    
    return monthly_totals

def get_part_time_wages_role(start_mmyyyy, end_mmyyyy,role):
    """
    Calculates the total wage expenditure for part-time employees of a specific role for each month between two months (inclusive).

    Args:
        start_mmyyyy (str): Start month-year in MMYYYY format.
        end_mmyyyy (str): End month-year in MMYYYY format.
        role (str): The role of the employees.

    Returns:
        list: A list of total wage expenditures for each month.
    """
    start_month = int(start_mmyyyy[:2])
    start_year = int(start_mmyyyy[2:])
    end_month = int(end_mmyyyy[:2])
    end_year = int(end_mmyyyy[2:])
    monthly_expenditures = []
    current_month = start_month
    current_year = start_year
    while (current_year < end_year or (current_year == end_year and current_month <= end_month)):
        query = f"""
            SELECT e.name, e.wage, s.starttime, s.endtime, s.role
            FROM Employees e
            JOIN Schedules s ON e.emp_id = s.emp_id
            WHERE e.status = 'Part Time'
            AND YEAR(s.week) = {current_year}
            AND MONTH(s.week) = {current_month}
            AND s.role = '{role}'
        """
        result = execute_query(query)
        total_wage_expenditure = 0.0
        for row in result:
            wage = float(row['wage'])
            shift_start = row['starttime']
            shift_end = row['endtime']
            hours_worked = (shift_end - shift_start).total_seconds() / 3600.0
            shift_wage_expenditure = wage * hours_worked
            total_wage_expenditure += shift_wage_expenditure
        monthly_expenditures.append(total_wage_expenditure)

        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
    
    return monthly_expenditures