import pymysql


# Establish a secure connection to the MySQL database using pymysql
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='root',  # Replace with actual password or environment variable
    port=3307,  # Adjust if necessary
    database='mflg'
)

print("DB connected successfully!")

query = "SELECT * FROM table_name"
cursor = connection.cursor()

cursor.execute("SELECT * FROM Wage")
results = cursor.fetchall()

for row in results:
  print(row)

cursor.execute("SELECT * FROM Employees")
results2 = cursor.fetchall()
for row in results2:
  print(row)

