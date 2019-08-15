import mysql.connector

#check connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)
