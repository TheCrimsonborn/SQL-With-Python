import mysql.connector

#This codeblock connects our script to the database.
mydb=mysql.connector.connect(
    host="localhost", #or server's nameserver
    user="root",
    password="root",
    database = "mydatabase"
)

mycursor=mydb.cursor()

# This code creates database.
# mycursor.execute("CREATE DATABASE mydatabase")

# This code shows all databases.
# mycursor.execute("SHOW DATABASES")

#This code is adding table to current database.
mycursor.execute("CREATE TABLE customers (name VARCHAR(255),address VARCHAR(255)) ")

#Prints the "SHOW DATABASES" command.
for x in mycursor:
    print(x)