import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Rahul@123"
)

# initalizing cursor
mycursor = mydb.cursor()

# show table
mycursor.execute("""SELECT * FROM test1.test_table;""")
for i in mycursor.fetchall():
    print(i)
mydb.close()
