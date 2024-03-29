# testing
from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def testing() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'mflg'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM employees')
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result


@app.route('/')
def index() -> str:
    return json.dumps({'employees': testing()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')