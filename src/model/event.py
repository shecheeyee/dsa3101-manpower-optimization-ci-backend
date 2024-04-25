# Import the execute_query function from db_utils.py
from db_utils import execute_query

# Function to create a new event
def create_event(data):
    mapped_fields = {
        'id': 'event_id',
        'eventName': 'event_name',
        'eventDate': 'date',
        'eventSession': 'event_period',
        'numPax': 'num_pax',
        'staffReq': 'staffReq',
        'remark': 'remark'
    }
    
    db_fields = []
    db_values = []
    
    for key, value in data.items():
        if key in mapped_fields:
            db_fields.append(mapped_fields[key])
            db_values.append(f"'{value}'" if isinstance(value, str) else str(value))
    
    field_names = ', '.join(db_fields)
    field_values = ', '.join(db_values)
    
    query = f"INSERT INTO Events ({field_names}) VALUES ({field_values})"
    execute_query(query)


# Function to retrieve all events
def get_all_events():
    query = "SELECT * FROM Events"
    # Assuming execute_query is properly implemented elsewhere
    events_from_db = execute_query(query)
    
    # Map database rows to frontend Event format
    events_for_frontend = []
    for event in events_from_db:
        mapped_event = {
            'id': event['event_id'],  # Assuming 'event_id' is the primary key
            'eventName': event['event_name'],
            'eventDate': event['date'].strftime('%Y-%m-%d'),  # Format date as string
            'eventSession': event['event_period'],  # Convert to Enum
            'numPax': event['num_pax'],
            'staffReq': event['staffReq'],
            'remark': event['remark']
        }
        events_for_frontend.append(mapped_event)
    
    return events_for_frontend

# Function to update an event
def update_event(event_id, update_data):
    mapped_fields = {
        'id': 'event_id',
        'eventName': 'event_name',
        'eventType': 'event_type',
        'eventDate': 'date',
        'eventSession': 'event_period',
        'numPax': 'num_pax',
        'staffReq': 'staffReq',
        'remark': 'remark'
    }
    
    update_fields = []
    
    for key, value in update_data.items():
        if key in mapped_fields:
            db_field = mapped_fields[key]
            db_value = f"'{value}'" if isinstance(value, str) else str(value)
            update_fields.append(f"{db_field} = {db_value}")
    
    set_clause = ", ".join(update_fields)
    query = f"UPDATE Events SET {set_clause} WHERE event_id = {event_id}"
    execute_query(query)

# Function to delete an event
def delete_event(event_id):
    query = f"DELETE FROM Events WHERE event_id = {event_id}"
    execute_query(query)
