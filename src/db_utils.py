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
            result = cursor.fetchall()
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