from db_utils import execute_query

def create_event(data):
    """
    Creates a new event in the database.

    Args:
        data (dict): A dictionary containing event data.

    Returns:
        None
    """
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

def get_all_events():
    """
    Retrieves all events from the database.

    Returns:
        list: A list of dictionaries containing event details.
    """
    query = "SELECT * FROM Events"
    events_from_db = execute_query(query)
    
    events_for_frontend = []
    for event in events_from_db:
        mapped_event = {
            'id': event['event_id'],
            'eventName': event['event_name'],
            'eventDate': event['date'].strftime('%Y-%m-%d'),
            'eventSession': event['event_period'],
            'numPax': event['num_pax'],
            'staffReq': event['staffReq'],
            'remark': event['remark']
        }
        events_for_frontend.append(mapped_event)
    
    return events_for_frontend

def update_event(event_id, update_data):
    """
    Updates an event in the database.

    Args:
        event_id (int): The ID of the event to be updated.
        update_data (dict): A dictionary containing updated event data.

    Returns:
        None
    """
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

def delete_event(event_id):
    """
    Deletes an event from the database.

    Args:
        event_id (int): The ID of the event to be deleted.

    Returns:
        None
    """
    query = f"DELETE FROM Events WHERE event_id = {event_id}"
    execute_query(query)
