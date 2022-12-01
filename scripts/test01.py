import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin1234",
  database="facu"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Tickets")

tickets = mycursor.fetchall()

for ticket in tickets:
    print(ticket)