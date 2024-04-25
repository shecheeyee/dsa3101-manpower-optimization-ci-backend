## DSA3101 BACKEND
This is the backend for the DSA3101 project. It is a RESTful API that provides endpoints for the frontend to interact with the database. The backend is built using Flask, a Python web framework. The database used is mySQL.

### How to run the backend
1. git clone the repository
2. `docker-compose build --no-cache`
3. `docker-compose up`
4. Try the endpoints using Postman or any other API testing tool

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
1. Create Individual Employee: POST /employee
1. Create Mutilple Employees: POST /employees
2. Get Employees: GET /employee
3. Update Employee: PUT /employee/<emp_id>
4. Delete Employee: DELETE /employee/<emp_id>
5. Get Wage: GET /wage
6. Create Event: POST /event
6. Create Individual Event: POST /event
7. Get Mutilple Events: GET /events
8. Update Event: PUT /event/<event_id>
9. Delete Event: DELETE /event/<event_id>
10. Create Schedule: POST /schedule
11. Get Schedules: GET /schedule
12. Store Optimal Schedule: POST /post_schedule
13. Update Schedule: PUT /schedule/<schedule_id>
14. Delete Schedule: DELETE /schedule/<schedule_id>
15. Post Past Demand: POST /post_past_demand
16. Get Past Demand: GET /get_past_demand
17. Post Demand Forecast: POST /post_demand_forecast
18. Get Demand Forecast: GET /get_demand_forecast

## Contributors
![BACKEND TEAM](images/good_old_days.jpg)
