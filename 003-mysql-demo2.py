'''
SCHOOL DATABASE (The Database created with MySQL Workbench IDE)
'''
from datetime import date
import mysql.connector

#Adding Student with inputs.
def addStudent(StudentNumber,Name,Surname,BirthDate,Gender):
    connection = mysql.connector.connect(host="localhost", user="root", password="root", database = "schooldb")
    cursor = connection.cursor()

    sql= "INSERT INTO students(StudentNumber,Name,Surname,BirthDate,Gender) VALUES (%s,%s,%s,%s,%s)"
    values = (StudentNumber,Name,Surname,BirthDate,Gender)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} student(s) added.')
        print(f'the id of the last student added: {cursor.lastrowid} ')

    except mysql.connector.Error as err:
        print('Error: ',err)
    finally:
        connection.close()
        print('Database connection closed!')

list=[]
while True:
    StudentNumber = int(input('Student Number: '))
    Name = input('Student Name: ')
    Surname = input('Student Surname: ')
    SBirthDate = (input('Student BirthDate (yyyy,mm,dd): '))
    Gender = input('Student Gender: ')
    year, month, day = map(int, SBirthDate.split(','))
    BirthDate = date(year, month, day)

    list.append((StudentNumber,Name,Surname,BirthDate,Gender))

    nextRecord=input("Will you add a new record? (y/n)")
    if nextRecord =="n":
        print("The record has been added to the database.")
        print(list)
        break




# addStudent(StudentNumber,Name,Surname,BirthDate,Gender)
