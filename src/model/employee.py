# Import the execute_query function from db_utils.py
from db_utils import execute_query

# Function to create a new employee
# Import the execute_query function from db_utils.py
from db_utils import execute_query

# Function to create a new employee with schedules
def create_employee(data):
    # Extract employee information
    emp_data = {
        'first_name': data['full_name'].split()[0],  # Split full_name into first_name and last_name
        'last_name': data['full_name'].split()[1] if ' ' in data['full_name'] else '',  # Handle cases where full_name has no space
        'wage': data['wage'],
        'primary_role': data['role'],
        'secondary_role': data['secondary_role']
    }
    
    # Create the INSERT query for Employees table
    emp_fields = ', '.join(emp_data.keys())
    emp_values = ', '.join(f"'{value}'" if isinstance(value, str) else str(value) for value in emp_data.values())
    emp_query = f"INSERT INTO Employees ({emp_fields}) VALUES ({emp_values})"
    
    # Execute the query to insert employee data
    result = execute_query(emp_query)
    emp_id = result.lastrowid  # Get the auto-generated emp_id
    
    # Extract and insert schedules for each weekday
    for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        if data[day] is not None:
            schedule_data = {
                'emp_id': emp_id,
                'week': data[day]['week'],
                'day': day.capitalize(),
                'shift': data[day]['shift'],
                'role': data[day]['role']
            }
            # Create the INSERT query for Schedules table
            schedule_fields = ', '.join(schedule_data.keys())
            schedule_values = ', '.join(f"'{value}'" if isinstance(value, str) else str(value) for value in schedule_data.values())
            schedule_query = f"INSERT INTO Schedules ({schedule_fields}) VALUES ({schedule_values})"
            
            # Execute the query to insert schedule data
            execute_query(schedule_query)


# Function to retrieve all employees
def get_all_employees():
    query = """
        SELECT e.emp_id, e.first_name, e.last_name,
               e.primary_role, e.secondary_role, e.wage, e.status, e.address,
               a.week, a.mon, a.tues, a.wed, a.thur, a.fri, a.sat, a.sun
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
            'name': f"{row['first_name']} {row['last_name']}",
            'role': row['primary_role'],
            'wage': row['wage'],
            'type': row['status'],
            'mon': row['mon'],
            'tues': row['tues'],
            'wed': row['wed'],
            'thur': row['thur'],
            'fri': row['fri'],
            'sat': row['sat'],
            'sun': row['sun']
        }
        employees.append(employee)
    
    return employees


# Function to update an employee
def update_employee(emp_id, update_data):
    update_fields = []
    for key, value in update_data.items():
        update_fields.append(f"{key} = '{value}'")
    set_clause = ", ".join(update_fields)
    query = f"UPDATE Employees SET {set_clause} WHERE emp_id = {emp_id}"
    # Execute the query using execute_query function
    execute_query(query)

# Function to delete an employee
def delete_employee(emp_id):
    query = f"DELETE FROM Employees WHERE emp_id = {emp_id}"
    # Execute the query using execute_query function
    execute_query(query)
