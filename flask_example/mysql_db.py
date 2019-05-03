import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    passwd="password",
    database="test_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM test_table")

myresults = mycursor.fetchall()

print(myresults)

for x in myresults:
    print(x)
