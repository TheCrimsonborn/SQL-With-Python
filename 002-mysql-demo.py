'''
SCHOOL DATABASE (The Database created with MySQL Workbench IDE)
'''
from datetime import date
import mysql.connector

#Adding Student with variables.
def addStudent():
    connection = mysql.connector.connect(host="localhost", user="root", password="root", database = "schooldb")
    cursor = connection.cursor()

    sql= "INSERT INTO students(StudentNumber,Name,Surname,BirthDate,Gender) VALUES (%s,%s,%s,%s,%s)"
    values = (101,'John','Doe', date(2000,1,1),'M')

    cursor.execute(sql,values)

    try:
        connection.commit()
    except mysql.connector.Error as err:
        print('Error: ',err)
    finally:
        connection.close()
        print('Database connection closed!')

addStudent()
