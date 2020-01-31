import mysql.connector
db_connection = mysql.connector.connect(
host="localhost",
user="root",
passwd="root",
database="SensorData"
  )
db_cursor = db_connection.cursor()
#Here creating database table as student'
db_cursor.execute("CREATE TABLE SensorR (Date DATETIME, Temp INT, Humidity INT , Pressure INT)")
#db_cursor.execute("CREATE TABLE studentl (id INT, name INT)")
#Get database table'
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
    print(table)