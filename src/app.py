# testing
from typing import List, Dict
from flask import Flask, request, jsonify
from flask_cors import CORS
from db_utils import execute_query
from model.employee import  create_employee, create_employees, update_employee, get_all_employees, delete_employee, get_full_time_wages, get_part_time_wages, get_full_time_wages_role, get_part_time_wages_role
from demand_forecast import seven_days_demand_forecast
from model.event import create_event, update_event, get_all_events, delete_event
from model.schedule import create_schedule, update_schedule, get_all_schedules, delete_schedule
from algo import staffing_algorithm
import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
CORS(app)

# Function to create a new employee individually
@app.route('/employee', methods=['POST'])
def create_new_employee():
    employee_data = request.json
    a = create_employee(employee_data)
    return jsonify({'message': 'Employee created successfully'}), 201

# Function to create employees from the uploaded csv
@app.route('/employees', methods=['POST'])
def create_new_employees():
    try:
        data = request.get_json()

        if not isinstance(data, list):
            return jsonify({'error': 'Invalid data format, expected list of dictionaries'}), 400

        # Process each row in the CSV data
        a = create_employees(data)
        app.logger.error(a)
        return jsonify({'message': 'Employees created successfully'}), 200
    except Exception as e:
        app.logger.error("Error processing CSV data: %s", e)
        return jsonify({'error': 'Failed to process CSV data'}), 500

# Function to retrieve all employees
@app.route('/employee', methods=['GET'])
def get_employees():
    employees = get_all_employees()
    return employees

# Function to update an employee
@app.route('/employee/<int:emp_id>', methods=['PUT'])
def update_e(emp_id):
    update_data = request.json
    a = update_employee(emp_id, update_data)
    return jsonify({'message': f'Employee with ID {emp_id} updated successfully'+ str(a)}), 200

# Function to delete an employee
@app.route('/employee/<int:emp_id>', methods=['DELETE'])
def delete_e(emp_id):
    delete_employee(emp_id)
    return jsonify({'message': f'Employee with ID {emp_id} deleted successfully'}), 200
    
# Function to create a new event individually
@app.route('/event', methods=['POST'])
def create_new_event():
    event_data = request.json
    create_event(event_data)
    return jsonify({'message': 'Event created successfully'}), 201

# Function to retrieve all events
@app.route('/event', methods=['GET'])
def get_events():
    events = get_all_events()
    return events

# Function to update an event
@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event_endpoint(event_id):
    update_data = request.json
    update_event(event_id, update_data)
    return jsonify({'message': f'Event with ID {event_id} updated successfully'}), 200

# Function to delete an event
@app.route('/event/<int:event_id>', methods=['DELETE'])
def delete_event_endpoint(event_id):
    delete_event(event_id)
    return jsonify({'message': f'Event with ID {event_id} deleted successfully'}), 200

# Function to create schedules manually
@app.route('/schedule', methods=['POST'])
def create_new_schedule():
    schedule_data = request.json
    a = create_schedule(schedule_data)
    return jsonify({'message': 'Schedule created successfully' + str(a)}), 201

# Function to get all schedules in databave
@app.route('/schedule', methods=['GET'])
def get_schedules():
    schedules = get_all_schedules()
    return jsonify(schedules)

# Function to call our algorithm to generate the schedule
@app.route("/generate_schedule", methods=["POST"])
def store_opt_schedule():
    working_hours_limit = request.json
    ft_hours = working_hours_limit["maxHrFT"]
    pt_hours = working_hours_limit["maxHrPT"]
    # staffing_algorithm() function executes the scheduling algorithm and stores the result in the database
    staffing_algorithm(ft_hours=ft_hours, pt_hours=pt_hours)
    return jsonify({"message": "Data stored successfully"})

# Function to update a schedule
@app.route('/schedule/<int:schedule_id>', methods=['PUT'])
def update_schedule_endpoint(schedule_id):
    update_data = request.json
    update_schedule(schedule_id, update_data)
    return jsonify({'message': f'Schedule with ID {schedule_id} updated successfully'}), 200

# Function to delete a schedule
@app.route('/schedule/<int:schedule_id>', methods=['DELETE'])
def delete_schedule_endpoint(schedule_id):
    delete_schedule(schedule_id)
    return jsonify({'message': f'Schedule with ID {schedule_id} deleted successfully'}), 200

# Function to post past demand
@app.route("/post_past_demand", methods=["POST"])
def post_past_demand():
    csv_file = request.files['file']
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
            field_names = f"Date, Day, Time, actualCustomers"
            field_values = f"DATE '{row['Date']}', '{row['Day']}', TIME '{row['Time']}', '{row['Customers']}'"
            query = f"INSERT INTO PastDemand ({field_names}) VALUES ({field_values})"
            execute_query(query)
    return jsonify({"message": "Data stored successfully"})

# Function to get past demand
@app.route("/get_past_demand", methods=["GET"])
def get_past_demand():
    query = "SELECT * FROM PastDemand"
    result = execute_query(query)
    if 'error' in result:
        return jsonify(result), 500
    else:
        past_demand_data = [{'Date': row["Date"], 'Day': row["Day"], 'Time': str(row["Time"]), "actualCustomers": row["actualCustomers"]} for row in result]
        return past_demand_data

# Function to post demand forecast
@app.route("/post_demand_forecast", methods=["POST"])
def store_demand_forecast():
    # Delete all rows from DemandForecast table
    query = "DELETE FROM DemandForecast"
    execute_query(query)

    # Forecast demand for today and next 6 days
    forecast_demand = seven_days_demand_forecast()

    # Store forecasted demand in the database
    for index, row in forecast_demand.iterrows():
        field_names = f"Date, Day, Time, expectedCustomers"
        field_values = f"DATE '{row['Date']}', '{row['Day']}', TIME '{row['Time']}', '{row['ExpectedCustomers']}'"
        query = f"INSERT INTO DemandForecast ({field_names}) VALUES ({field_values})"
        execute_query(query)
    return jsonify({"message": "Data stored successfully"})

# Function to get demand forecase
@app.route("/get_demand_forecast", methods=["GET"])
def get_demand_forecast():
    query = "SELECT * FROM DemandForecast"
    result = execute_query(query)
    if 'error' in result:
        return jsonify(result), 500
    else:
        demand_forecast_data = [{'Date': row["Date"], 'Day': row["Day"], 'Time': str("Time"), "actualCustomers": row["expectedCustomers"]} for row in result]
        return demand_forecast_data
    
# Function to get total cost of 
@app.route('/total_cost_status', methods=['GET'])
def calculate_total_expenditure_status():
    # Get start_mmyy and end_mmyy from request data
    request_data = request.json
    start_mmyy = request_data.get('start_mmyy')
    end_mmyy = request_data.get('end_mmyy')
    
    # Calculate total expenditure for full-time employees between the specified months
    full_time_expenditure = get_full_time_wages(start_mmyy, end_mmyy)
    
    # Calculate total expenditure for part-time employees between the specified months
    part_time_expenditure = get_part_time_wages(start_mmyy, end_mmyy)
    
    # Combine the total expenditures into a single list
    total_expenditure = {
        'full_time_expenditure': full_time_expenditure,
        'part_time_expenditure': part_time_expenditure
    }
    return total_expenditure

@app.route('/total_cost_role', methods=['GET'])
def calculate_total_expenditure_role():
    # Get start_mmyy and end_mmyy from request data
    request_data = request.json
    start_mmyy = request_data.get('start_mmyy')
    end_mmyy = request_data.get('end_mmyy')
    
    manager_expenditure = [ft_wage + pt_wage for ft_wage, pt_wage in zip(get_full_time_wages_role(start_mmyy, end_mmyy, 'Manager'), get_part_time_wages_role(start_mmyy, end_mmyy, 'Manager'))]
    service_expenditure = [ft_wage + pt_wage for ft_wage, pt_wage in zip(get_full_time_wages_role(start_mmyy, end_mmyy, 'Service'), get_part_time_wages_role(start_mmyy, end_mmyy, 'Service'))]
    kitchen_expenditure = [ft_wage + pt_wage for ft_wage, pt_wage in zip(get_full_time_wages_role(start_mmyy, end_mmyy, 'Kitchen'), get_part_time_wages_role(start_mmyy, end_mmyy, 'Kitchen'))]
    
    # Combine the total expenditures into a single list
    total_expenditure = {
        'Manager': manager_expenditure,
        'Service': service_expenditure,
        'Kitchen': kitchen_expenditure
    }
    return total_expenditure

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)