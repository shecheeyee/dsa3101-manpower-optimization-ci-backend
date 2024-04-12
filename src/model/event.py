# Import the execute_query function from db_utils.py
from db_utils import execute_query

# Function to create a new event
def create_event(data):
    fields = []
    for key, value in data.items():
        if value is not None:
            fields.append((key, value))
    field_names = ', '.join(field[0] for field in fields)
    field_values = ', '.join(f"'{field[1]}'" if isinstance(field[1], str) else str(field[1]) for field in fields)
    query = f"INSERT INTO Events ({field_names}) VALUES ({field_values})"
    # Execute the query using execute_query function
    execute_query(query)

# Function to retrieve all events
def get_all_events():
    query = "SELECT event_id, date, event_type, event_name, num_pax, time, CAST(duration AS CHAR) AS duration FROM Events"
    # Execute the query using execute_query function
    events = execute_query(query)
    
    # Convert timedelta duration to string
    for event in events:
        event['date'] = str(event['date'])  # Convert date to string
        event['time'] = str(event['time'])  # Convert time to string
        event['duration'] = str(event['duration'])  # Convert duration to string
    
    return events


# Function to update an event
def update_event(event_id, update_data):
    update_fields = []
    for key, value in update_data.items():
        update_fields.append(f"{key} = '{value}'")
    set_clause = ", ".join(update_fields)
    query = f"UPDATE Events SET {set_clause} WHERE event_id = {event_id}"
    # Execute the query using execute_query function
    execute_query(query)

# Function to delete an event
def delete_event(event_id):
    query = f"DELETE FROM Events WHERE event_id = {event_id}"
    # Execute the query using execute_query function
    execute_query(query)
