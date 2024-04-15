import pymysql

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': 3307,
    'database': 'mflg'
}

def execute_query(query):
    try:
        connection = pymysql.connect(**config)
        cursor = connection.cursor()
        cursor.execute(query)
        if query.strip().lower().startswith('select'):
            # Fetch column names from cursor description
            column_names = [desc[0] for desc in cursor.description]
            # Fetch all rows
            rows = cursor.fetchall()
            # Convert rows to dictionaries
            result = []
            for row in rows:
                result.append(dict(zip(column_names, row)))
            return result
        else:
            connection.commit()
            return {'message': 'Query executed successfully.'}
    except pymysql.Error as error:
        return {'error': str(error)}
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection is not None:
            connection.close()
