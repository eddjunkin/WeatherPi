import mysql.connector
db_connection = mysql.connector.connect(
host="localhost",
user="root",
passwd="root",
database="SensorData"
  )
db_cursor = db_connection.cursor()
SensorR_sql_query = "INSERT INTO SensorR(Date,Temp,Humidity,Pressure) VALUES('2020-01-25 12:23:10', 65, 24, 90)"
#Execute cursor and pass query as well as student data
SensorP_sql_query = "INSERT INTO SensorP(Date,Temp,Humidity,Pressure) VALUES('2020-01-26 12:23:10', 63, 24, 90)"
db_cursor.execute(SensorR_sql_query)
db_cursor.execute(SensorP_sql_query)
#Execute cursor and pass query of employee and data of employee
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")