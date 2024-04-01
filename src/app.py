# testing
from typing import List, Dict
from flask import Flask, request, jsonify
from flask_cors import CORS
from db_utils import execute_query
from model.employee import  create_employee, update_employee, get_all_employees, delete_employee
import json
import csv

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


if __name__ == '__main__':
    app.run(host='0.0.0.0')