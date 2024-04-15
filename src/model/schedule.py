# Import the execute_query function from db_utils.py
from db_utils import execute_query

def create_schedule(data):
    mapped_fields = {
        'id': 'scheduleId',
        'employeeId': 'emp_id',
        'start': 'starttime',
        'end': 'endtime',
        'shift': 'shift',
        'day': 'day',
        'role': 'role',
        'week': 'week'
    }

    db_fields = []
    db_values = []

    for key, value in data.items():
        if key in mapped_fields:
            db_fields.append(mapped_fields[key])
            db_values.append(f"'{value}'" if isinstance(value, str) else str(value))

    field_names = ', '.join(db_fields)
    field_values = ', '.join(db_values)

    query = f"INSERT INTO Schedules ({field_names}) VALUES ({field_values})"
    execute_query(query)


def get_all_schedules():
    query = "SELECT * FROM Schedules"
    schedules_from_db = execute_query(query)

    schedules_for_frontend = []
    for schedule in schedules_from_db:
        mapped_schedule = {
            'id': schedule['scheduleId'],
            'employeeId': schedule['emp_id'],
            'start': schedule['starttime'].strftime('%H:%M:%S'),
            'end': schedule['endtime'].strftime('%H:%M:%S'),
            'shift': schedule['shift'],
            'day': schedule['day'],
            'role': schedule['role'],
            'week': schedule['week'].strftime('%Y-%m-%d')
        }
        schedules_for_frontend.append(mapped_schedule)

    return schedules_for_frontend


def update_schedule(schedule_id, update_data):
    mapped_fields = {
        'employeeId': 'emp_id',
        'start': 'starttime',
        'end': 'endtime',
        'shift': 'shift',
        'day': 'day',
        'role': 'role',
        'week': 'week'
    }

    update_fields = []

    for key, value in update_data.items():
        if key in mapped_fields:
            db_field = mapped_fields[key]
            db_value = f"'{value}'" if isinstance(value, str) else str(value)
            update_fields.append(f"{db_field} = {db_value}")

    set_clause = ", ".join(update_fields)
    query = f"UPDATE Schedules SET {set_clause} WHERE scheduleId = {schedule_id}"
    execute_query(query)


def delete_schedule(schedule_id):
    query = f"DELETE FROM Schedules WHERE scheduleId = {schedule_id}"
    execute_query(query)
