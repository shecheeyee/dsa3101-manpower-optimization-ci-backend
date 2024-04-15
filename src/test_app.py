# unit testing
import pytest
from app import app
from unittest.mock import patch
from db_utils import execute_query
from datetime import datetime



@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# def test_create_employee(client):
#     # testing respoinse with random json data
#     test_employee_data = {
#         "full_name": "John Doe",
#         "wage": 10,
#         "role": "Manager",
#         "secondary_role": "Manager",
#     }
#     response = client.post('/employees', json=test_employee_data)
#     assert response.status_code == 201
#     assert response.json['message'] == 'Employee created successfully'

def test_get_employees(client):
    response = client.get('/employees')
    assert response.status_code == 200

def test_update_employee(client):
    update_data = {'name': 'Jane Doe'}
    employee_id = 99  # Assuming an existing employee with this ID
    response = client.put('/employees/{}'.format(employee_id), json=update_data)
    assert response.status_code == 200
    assert response.json['message'] == f'Employee with ID {employee_id} updated successfully'

def test_delete_employee(client):
    employee_id = 99  # Assuming an existing employee with this ID
    response = client.delete('/employees/{}'.format(employee_id))
    assert response.status_code == 200
    assert response.json['message'] == f'Employee with ID {employee_id} deleted successfully'

def test_get_wage(client):
    response = client.get('/wage')
    assert response.status_code == 200
    # Add assertions to check the structure of the returned wage data

def test_store_demand_forecast(client):
    # Send a POST request with the forecast data (consider using JSON)
    response = client.post('/post_demand_forecast')

    # Assert expected response
    # Not testing the actual data storage in the database, but the response message
    assert response.status_code == 200
    assert response.json['message'] == 'Data stored successfully'

def test_get_demand_forecast(client):

    response = client.get('/get_demand_forecast')

    assert response.status_code == 200
    # Assert the structure and content of the returned data
    data = response.json
    date_obj_0 = datetime.strptime(data[0]['Date'], '%a, %d %b %Y %H:%M:%S %Z')
    formatted_date_0 = date_obj_0.strftime('%Y-%m-%d')
    date_obj_1 = datetime.strptime(data[-1]['Date'], '%a, %d %b %Y %H:%M:%S %Z')
    formatted_date_1 = date_obj_1.strftime('%Y-%m-%d')

    # not testing prediction as it is not deterministic
    assert len(data) == 84  # 7 days * 12 hours, 1 week of prediction
    assert formatted_date_0 ==  '2024-04-14'
    assert data[0]['Day'] == 'Sunday'
    assert data[0]['Time'] == '10:00:00' 
    assert formatted_date_1 == '2024-04-20'
    assert data[-1]['Day'] == 'Saturday'
    assert data[-1]['Time'] == '21:00:00'  
    
    # clear the data
    query = 'DELETE FROM DemandForecast'
    execute_query(query)
    




# def test_post_past_demand(client):
#     # Sample CSV data (assuming a CSV file with headers)
#     csv_data = """
#     Date,Day,Time,Customers
#     2024-04-10,Wednesday,10:00,80
#     2024-04-10,Wednesday,11:00,95
#     """

#     # Mock the request.files object to simulate a CSV upload
#     with patch('flask.request.files', {'file': io.BytesIO(csv_data.encode('utf-8'))}):
#         response = client.post('/post_past_demand')

#     assert response.status_code == 200
#     assert response.json['message'] == "Data stored successfully"

def test_get_past_demand(client):
    response = client.get('/get_past_demand')

    assert response.status_code == 200
    # Assert the structure and content of the returned data
    data = response.json
    assert len(data) == 2160  # len of csv file
    date_obj_0 = datetime.strptime(data[0]['Date'], '%a, %d %b %Y %H:%M:%S %Z')
    formatted_date_0 = date_obj_0.strftime('%Y-%m-%d')
    date_obj_1 = datetime.strptime(data[-1]['Date'], '%a, %d %b %Y %H:%M:%S %Z')
    formatted_date_1 = date_obj_1.strftime('%Y-%m-%d')
    assert formatted_date_0 == '2024-05-10'
    assert data[0]['Day'] == 'Friday'
    assert data[0]['Time'] == '10:00:00'  # Assuming time is stored as string
    assert data[0]['actualCustomers'] == 14
    assert formatted_date_1 == '2023-11-13'
    assert data[-1]['Day'] == 'Monday'
    assert data[-1]['Time'] == '21:00:00'  # Assuming time is stored as string
    assert data[-1]['actualCustomers'] == 12

