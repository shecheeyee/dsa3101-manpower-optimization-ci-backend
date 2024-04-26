# unit testing
import pytest
from app import app
from unittest.mock import patch
from datetime import datetime
from db_utils import execute_query




@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
        
def test_create_new_employee(client):
    # Sample employee data
    data = {
        'name': 'Test Employee',
        'role': 'Service',
        'email': 'test@example.com' 
    }

    # Make a POST request to the '/employee' endpoint
    response = client.post('/employee', json=data)

    # Assertations
    assert response.status_code == 201  # Check for successful creation status
    assert response.json['message'] == 'Employee created successfully'  # Check the response message

def test_get_employees(client):
    response = client.get('/employee')
    assert response.status_code == 200

def test_update_employee(client):
    update_data = {'name': 'Jane Doe', 
                   'role':'Manager',
                   'secondaryRole':'Manager',
                   'wage':10,
                   'employementType':'Full Time'}
    employee_id = 1  # Assuming an existing employee with this ID
    response = client.put('/employee/{}'.format(employee_id), json=update_data)
    assert response.status_code == 200
    assert response.json['message'] == f'Employee with ID {employee_id} updated successfullyNone'

def test_delete_employee(client):
    employee_id = 1  # Assuming an existing employee with this ID
    response = client.delete('/employee/{}'.format(employee_id))
    print(response.json)
    assert response.status_code == 200
    assert response.json['message'] == f'Employee with ID {employee_id} deleted successfully'

# Test for event creation
def test_create_new_event(client):
    data = {
        'title': 'Test Event',
        'start_date': '2024-04-28',
        'end_date': '2024-04-28',
        'description': 'This is a test event' 
    }

    response = client.post('/event', json=data)
    assert response.status_code == 201
    assert response.json['message'] == 'Event created successfully'

# Test for retrieving all events
def test_get_events(client):
    response = client.get('/event')
    assert response.status_code == 200
    # Additionally, you might want to check the structure of the returned events data

# Test for updating an event
def test_update_event(client):
    event_id = 1  # Assuming event with ID 1 exists
    data = {'title': 'Updated Test Event'}
    response = client.put(f'/event/{event_id}', json=data)
    assert response.status_code == 200
    assert response.json['message'] == f'Event with ID {event_id} updated successfully'

# Test for deleting an event
def test_delete_event(client):
    event_id = 2  # Assuming event with ID 2 exists
    response = client.delete(f'/event/{event_id}')
    assert response.status_code == 200
    assert response.json['message'] == f'Event with ID {event_id} deleted successfully'
    

# Test for creating a new schedule
def test_create_new_schedule(client):
    data = {
        # Add your sample schedule data here (employee IDs, shifts, etc.)
    }
    response = client.post('/schedule', json=data) 
    assert response.status_code == 201
    # You might want to check the structure of the 'a' value in the response as well

# Test for getting all schedules
def test_get_all_schedules(client):
    response = client.get('/schedule')
    assert response.status_code == 200
    # Further validation to ensure that the returned schedules data is as expected

# # Test for generating an optimized schedule
# def test_generate_schedule(client):
#     data = {"maxHrFT": 200, "maxHrPT": 100}  # Example working hour limits
#     response = client.post("/generate_schedule", json=data)
#     assert response.status_code == 200
#     assert response.json['message'] == "Data stored successfully"

# Test for updating a schedule
def test_update_schedule(client):
    schedule_id = 1  # Assuming schedule with ID 1 exists
    data = {
         # Add some updated schedule data here
    }
    response = client.put(f'/schedule/{schedule_id}', json=data)
    assert response.status_code == 200
    assert response.json['message'] == f'Schedule with ID {schedule_id} updated successfully'

# Test for deleting a schedule
def test_delete_schedule(client):
    schedule_id = 2  # Assuming schedule with ID 2 exists
    response = client.delete(f'/schedule/{schedule_id}')
    assert response.status_code == 200
    assert response.json['message'] == f'Schedule with ID {schedule_id} deleted successfully'
    
    
# # Test for storing past demand data (with CSV upload)
# def test_post_past_demand(client, mocker):
#     csv_content = "Date,Day,Time,Customers\n2024-04-28,Sunday,10:00:00,20\n2024-04-29,Monday,11:00:00,15" 
#     csv_file = io.StringIO(csv_content) 

#     mocker.patch("app.execute_query")  # Mock database interactions

#     response = client.post("/post_past_demand", data={'file': (csv_file, 'test.csv')}) 

#     assert response.status_code == 200
#     assert response.json['message'] == "Data stored successfully"

# Test for getting past demand data
# def test_get_past_demand(client, mocker):
#     # Mock the return value of 'execute_query'
#     mocker.patch("app.execute_query", return_value=[
#         {"Date": "2024-04-28", "Day": "Sunday", "Time": "10:00:00", "actualCustomers": 20},
#         # Add more sample data if needed
#     ])

#     response = client.get("/get_past_demand")
#     assert response.status_code == 200
#     assert response.json == [  # Check the expected structure
#         {'Date': '2024-04-28', 'Day': 'Sunday', 'Time': '10:00:00', "actualCustomers": 20},
#         # ... more data
#     ]

# # Test for storing demand forecast
# def test_store_demand_forecast(client, mocker):
#     mocked_forecast = mocker.patch("app.seven_days_demand_forecast") 
#     mocked_forecast.return_value = pd.DataFrame({
#         'Date': ['2024-04-28', '2024-04-29'], 
#         'Day': ['Sunday', 'Monday'], 
#         'Time': ['10:00:00', '11:00:00'], 
#         'ExpectedCustomers': [10, 15]})

#     mocker.patch("app.execute_query")  # Mock database interactions

#     response = client.post("/post_demand_forecast")
#     assert response.status_code == 200
#     assert response.json['message'] == "Data stored successfully"
    
# # Test for getting demand forecast data
# def test_get_demand_forecast(client, mocker):
#     # Mock the return value of 'execute_query'
#     mocker.patch("app.execute_query", return_value=[
#         {"Date": "2024-04-28", "Day": "Sunday", "Time": "10:00:00", "expectedCustomers": 15},
#         {"Date": "2024-04-29", "Day": "Monday", "Time": "11:00:00", "expectedCustomers": 20},
#     ])

#     response = client.get("/get_demand_forecast")
#     assert response.status_code == 200
#     assert response.json == [
#         {'Date': '2024-04-28', 'Day': 'Sunday', 'Time': '10:00:00', "actualCustomers": 15}, 
#         {'Date': '2024-04-29', 'Day': 'Monday', 'Time': '11:00:00', "actualCustomers": 20} 
#     ]