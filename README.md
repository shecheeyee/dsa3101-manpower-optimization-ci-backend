## DSA3101 BACKEND
This is the backend for the DSA3101 project. It is a RESTful API that provides endpoints for the frontend to interact with the database. The backend is built using Flask, a Python web framework. The database used is mySQL.

### How to run the backend
1. git clone the repository
2. `docker-compose build --no-cache`
3. `docker-compose up`
4. Try the endpoints using Postman or any other API testing tool

### Endpoints
1. Create Employee: POST /employee
2. Get Employees: GET /employee
3. Update Employee: PUT /employee/<emp_id>
4. Delete Employee: DELETE /employee/<emp_id>
5. Get Wage: GET /wage
6. Create Event: POST /event
7. Get Events: GET /event
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