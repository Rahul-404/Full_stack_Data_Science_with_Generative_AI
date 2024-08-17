import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Rahul@123"
)

# initalizing cursor
mycursor = mydb.cursor()

# printing all databased
mycursor.execute("CREATE DATABASE IF NOT EXISTS test1")
mycursor.execute("CREATE TABLE IF NOT EXISTS test1.test_table (c1 INT, c2 VARCHAR(50), c3 INT, c4 FLOAT, c5 VARCHAR(20))")

mydb.close() # we suppose to call close all the time