# Import the execute_query function from db_utils.py
from db_utils import execute_query

# Function to create a new employee
def create_employee(data):
    fields = []
    for key, value in data.items():
        if value is not None:
            fields.append((key, value))
    field_names = ', '.join(field[0] for field in fields)
    field_values = ', '.join(f"'{field[1]}'" if isinstance(field[1], str) else str(field[1]) for field in fields)
    query = f"INSERT INTO Employees ({field_names}) VALUES ({field_values})"
    # Execute the query using execute_query function
    execute_query(query)

# Function to retrieve all employees
def get_all_employees():
    query = "SELECT * FROM Employees"
    # Execute the query using execute_query function and return the result
    return execute_query(query)

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
