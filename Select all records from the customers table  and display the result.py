import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="teste8"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers3")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
