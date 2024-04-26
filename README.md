## DSA3101 BACKEND
This is the backend for the DSA3101 project. It is a RESTful API that provides endpoints for the frontend to interact with the database. The backend is built using Flask, a Python web framework. The database used is mySQL.

To deploy this application along with the frontend, see our [deployment repo](https://github.com/kevin-pek/dsa3101-deployment).

### How to run the backend
1. git clone the repository
2. `docker-compose build --no-cache`
3. `docker-compose up -d`
4. Try the endpoints using Postman or any other API testing tool

### How to run unit tests
1. `docker-compose up -d`
2. Change db configurations in `db_utils.py` to the one for unit test
3. cd to `src`
4. `pytest` to see unit test results
5. Change db configurations back to original one and do `docker-compose down -v` to ensure no side effects

### Project Folder Structure
```plaintext
.
├── README.md
├── data
│   ├── csv
│   │   ├── 00-mock_emp_details.csv                 # synthetic data for employee details
│   │   ├── 01-mock_availability.csv                # synthetic data for employee availability
│   │   ├── 02-mock_events.csv                      # synthetic data for events 
│   │   ├── 03-mock_wage.csv                        # synthetic data for part-time employee wage
│   │   └── 04-mock_customer_demand_past.csv        # synthetic data for past customer demand 
│   └── json
│       ├── expected_customers.json                 # synthetic data for the expected number of customers per hour
│       └── public_holidays.json                    # data for public holidays in singapore
├── docker-compose.yml                              # docker-compose file for deploying the backend
├── images
│   └── good_old_days.jpg                           # backend team visiting our stakeholders :) 
├── mysql_db                                        # entrypoint for building database from docker image
│   ├── 00-create-db.sql                            # creates database
│   ├── 01-schema.sql                               # creates schema
│   ├── 02-load-data.sql                            # loads data from `data/csv`
│   └── custom.cnf                                  # custom configuration file for `mysql` image
└── src
    ├── Dockerfile                                  # Dockerfile for building flask container
    ├── algo.py                                     # algorithm to generate optimized schedules
    ├── app.py                                      # flask app
    ├── db_utils.py                                 # database utility file for query execution
    ├── demand_forecast.py                          # time series model to generate demand forecast
    ├── model
    │   ├── __init__.py
    │   ├── employee.py                             # functions for employee-related CRUD operations
    │   ├── event.py                                # functions for events-related CRUD operations
    │   └── schedule.py                             # functions for schedule-related CRUD operations
    ├── requirements.txt                            # dependencies for backend
    ├── tests
    │   ├── __init__.py
    │   ├── test_app.py                             # unit tests for endpoints
    │   └── test_utils.py                           # unit tests for other functions
    └── utils.py                                    # utility functions 
```


### Endpoints
| Route              | HTTP Method | Description                                                                                               |
|--------------------|-------------|-----------------------------------------------------------------------------------------------------------|
| /employee          | POST        | Create a new employee in the database along with their associated availability                           |
| /employee          | GET         | Retrieves all employees to be displayed on frontend                                                      |
| /employee/int:emp_id | PUT        | Updates an employee’s attributes identified by its ID including their availability                        |
| /employee/int:emp_id | DELETE     | Delete an employee identified by its ID and all availability associated with the employee                |
| /employees         | POST        | Create employees in the database from an uploaded CSV                                                    |
| /event             | POST        | Create a new event in the database                                                                        |
| /event             | GET         | Retrieve all events to be displayed on frontend                                                          |
| /event/int:event_id | PUT        | Update an event’s attribute identified by its ID                                                          |
| /event/int:event_id | DELETE     | Delete an event identified by its ID                                                                      |
| /schedule          | POST        | Create a new schedule in the database                                                                     |
| /schedule          | GET         | Retrieve all schedules to be displayed on frontend                                                        |
| /schedule/int:schedule_id | PUT   | Update a schedule identified by its ID                                                                     |
| /schedule/int:schedule_id | DELETE| Delete a schedule identified by its  ID                                                                    |
| /generate_schedule | POST        | Generate and store schedule using backend schedule generator algorithm based on employees availability |
| /post_past_demand  | POST        | Create past demand data in the database                                                                   |
| /get_past_demand   | GET         | Get past demand data to be displayed on frontend                                                         |
| /post_demand_forecast | POST     | Create demand forecast data in the database                                                               |
| /get_demand_forecast  | GET      | Get demand forecast data to be displayed on frontend                                                      |
| /total_cost_status | GET         | Calculates and return monthly total expenditure of Full Timers and Part Timers                             |
| /total_cost_role   | GET         | Calculates and return monthly total expenditure of the different roles, Manager, Service and Kitchen     |


## Contributors
![BACKEND TEAM](images/good_old_days.jpg)
