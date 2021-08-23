'''
SCHOOL DATABASE (The Database created with MySQL Workbench IDE)
'''
from datetime import date
import mysql.connector

#Adding many Students with list method.
connection = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="root", 
    database = "schooldb"
)

mycursor = connection.cursor()

sql = "INSERT INTO students(StudentNumber,Name,Surname,BirthDate,Gender) VALUES (%s,%s,%s,%s,%s)"
students=[
    ("103","Diego","Irving",date(1997,9,12),"M"),
    ("104","Renee","Farley",date(1999,2,1),"F"),
    ("105","Leena","Blake",date(1998,5,6),"F"),
    ("106","Keenan","Yates",date(2001,10,5),"M"),
    ("107","Hiba","Norton",date(2002,6,14),"F")
]

mycursor.executemany(sql,students)

try:
    connection.commit()
    print(f'{mycursor.rowcount} students added.')
    print(f'the id of the last student added: {mycursor.lastrowid} ')
except mysql.connector.Error as err:
    print('Error: ',err)
finally:
    connection.close()
    print('Database connection closed!')