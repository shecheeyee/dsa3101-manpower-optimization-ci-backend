# Import the execute_query function from db_utils.py
from db_utils import execute_query

# Function to create a new employee
def create_employee(data):
    # Extract employee data from the input dictionary
    name = data['name']
    primary_role = data['role']
    secondary_role = data['secondaryRole']
    wage = data['wage']
    status = data['employmentType']  # Employment status (e.g., full-time, part-time)
    
    query = "SELECT MAX(emp_id) FROM Employees"
    emp_id = execute_query(query)[0]['MAX(emp_id)']+1
    print(emp_id)
    # Prepare SQL query to insert into Employees table
    insert_employee_query = f"""
        INSERT INTO Employees (emp_id, first_name, last_name, dob, email, gender, primary_role, secondary_role, wage, status)
        VALUES ('{emp_id}', '{name}', '2000-12-12', 'abc@gmail.com', 'M', '{primary_role}', '{secondary_role}', {wage}, '{status}')
    """
    
    # Execute the insert query to add the employee to Employees table
    a = execute_query(insert_employee_query)

    # Prepare SQL query to insert into Availability table
    insert_availability_query = f"""
        INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun)
        VALUES  ({emp_id}, '2023-12-31',{data['mon']}, {data['tues']}, {data['wed']}, {data['thurs']}, {data['fri']}, {data['sat']}, {data['sun']})
    """
    execute_query(insert_availability_query)

    # Return the emp_id of the newly created employee
    return str(a) + str(secondary_role)

# Function to retrieve all employees
def get_all_employees():
    query = """
        SELECT e.emp_id, e.name,
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
            'name': f"{row['name']}",
            'role': row['primary_role'],
            'secondaryRole' : row['secondary_role'],
            'employmentType' : row['status'],
            'wage': row['wage'],
            'type': row['status'],
            'mon': row['mon'],
            'tues': row['tues'],
            'wed': row['wed'],
            'thurs': row['thur'],
            'fri': row['fri'],
            'sat': row['sat'],
            'sun': row['sun']
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
            SET mon = '{data.get('mon')}',
                tues = '{data.get('tues')}',
                wed = '{data.get('wed')}',
                thur = '{data.get('thur')}',
                fri = '{data.get('fri')}',
                sat = '{data.get('sat')}',
                sun = '{data.get('sun')}'
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
