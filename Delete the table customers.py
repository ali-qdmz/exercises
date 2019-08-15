import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="teacher"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql) 
