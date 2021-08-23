'''
SCHOOL DATABASE (The Database created with MySQL Workbench IDE)
'''
from datetime import date
import mysql.connector
from connection import connection

#Adding many Students with list method.

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, studentnumber,name,surname,birthdate,gender):
        self.studentnumber = studentnumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
    
    def saveStudent(self):
        sql = "INSERT INTO students(StudentNumber,Name,Surname,BirthDate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values= (self.studentnumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} students added.')
            print(f'the id of the last student added: {Student.mycursor.lastrowid} ')
        except mysql.connector.Error as err:
            print('Error: ',err)
        finally:
            Student.connection.close()
            print('Database connection closed!')


newStudent=Student("108","Johnny","Bravo",date(1996,7,12),"M")
newStudent.saveStudent()