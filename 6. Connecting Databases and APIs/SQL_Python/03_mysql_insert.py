import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Rahul@123"
)

# initalizing cursor
mycursor = mydb.cursor()

# insertion of record
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mycursor.execute("""INSERT INTO test1.test_table VALUES(3424 , 'rahul' , 234 , 546.26 , 'shelke')""")
mydb.commit()
mydb.close()
