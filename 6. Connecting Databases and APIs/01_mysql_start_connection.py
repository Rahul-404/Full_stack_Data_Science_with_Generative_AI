import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Rahul@123"
)

print(mydb)

# initalizing cursor
mycursor = mydb.cursor()

# printing all databased
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)