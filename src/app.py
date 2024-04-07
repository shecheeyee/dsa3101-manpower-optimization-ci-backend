# testing
from typing import List, Dict
from flask import Flask, request, jsonify
from flask_cors import CORS
from db_utils import execute_query
from model.employee import  create_employee, update_employee, get_all_employees, delete_employee
from demand_forecast import demand_forecast
import json
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/employees', methods=['POST'])
def create_new_employee():
    employee_data = request.json
    create_employee(employee_data)
    return jsonify({'message': 'Employee created successfully'}), 201

# Function to retrieve all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = get_all_employees()
    return jsonify({'employees': employees})

# Function to update an employee
@app.route('/employees/<int:emp_id>', methods=['PUT'])
def update_e(emp_id):
    update_data = request.json
    update_employee(emp_id, update_data)
    return jsonify({'message': f'Employee with ID {emp_id} updated successfully'}), 200

# Function to delete an employee
@app.route('/employees/<int:emp_id>', methods=['DELETE'])
def delete_e(emp_id):
    delete_employee(emp_id)
    return jsonify({'message': f'Employee with ID {emp_id} deleted successfully'}), 200

@app.route('/wage', methods=['GET'])
def get_wage():
    query = 'SELECT * FROM Wage'
    result = execute_query(query)
    if 'error' in result:
        return jsonify(result), 500
    else:
        wage_data = [{'day': row[0], 'role': row[1], 'wage': row[2]} for row in result]
        return jsonify({'wage': wage_data})

@app.route("/post_demand_forecast", methods=["POST"])
def store_demand_forecast():
    try:
        # Get the forecast data
        forecast_demand = demand_forecast()

        # Insert the forecast data into the database
        for date, day, time, hourly_customers in forecast_demand:
            field_names = f"Date, Day, Time, expectedCustomers"
            field_values = f"DATE'{date}', {day}, TIME '{time}', '{hourly_customers}'"
            query = f"INSERT INTO DemandForecast ({field_names}) VALUES ({field_values})"
            execute_query(query)
        return jsonify({"message": "Data stored successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/get_demand_forecast", methods=["GET"])
def get_demand_forecast():
    query = "SELECT * FROM DemandForecast"
    result = execute_query(query)
    demand_forecast_data = [{'Date': row[0], 'Day': row[1], 'Time': str(row[2]), "actualCustomers": row[3]} for row in result]
    return jsonify(demand_forecast_data)

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

@app.route("/get_past_demand", methods=["GET"])
def get_past_demand():
    query = "SELECT * FROM PastDemand"
    result = execute_query(query)
    past_demand_data = [{'Date': row[0], 'Day': row[1], 'Time': str(row[2]), "actualCustomers": row[3]} for row in result]
    return jsonify(past_demand_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')