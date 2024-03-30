# testing
from typing import List, Dict
from flask import Flask
import pymysql
import json
import csv

app = Flask(__name__)


config = {
        'user': 'root',
        'password': 'root',
        'host': 'mysql-db',
        'port': '3306',
        'database': 'mflg'
    }

            
def get_wage() -> List[Dict]:
    """
    Test: fetches wage data from the database and returns as a list of dictionaries.
    """
    config = config

    try:
        connection = pymysql.connect(**config)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Wage')
        result = cursor.fetchall()
        return [{'day': row[0], 'role': row[1], 'wage':row[2]} for row in result]  

    except Exception as e:
        print(f"Error fetching wage: {e}")
        return []  

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


@app.route('/')
def index() -> str:
    wage = get_wage()
    return json.dumps({'wage': employees})


if __name__ == '__main__':
    app.run(host='0.0.0.0')