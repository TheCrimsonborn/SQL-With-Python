import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "SELECT * FROM students WHERE id = %s"
        value  = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def deleteStudent(self,studentid):
        sql = "DELETE FORM students WHERE id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('Error:', err)

    def getClasses(self):
        sql = "SELECT * FROM class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def getStudentsByClassId(self,classid):
        sql = "SELECT * FROM students WHERE classid = %s"
        value  = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def addorEditStudent(self,student: Student):
        pass

    def addStudent(self, student: Student):        
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber,student.name, student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} student(s) added.')
        except mysql.connector.Error as err:
            print('Error:', err)

    def editStudent(self, student: Student):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classid=%s where id=%s"
        value = (student.studentNumber,student.name, student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} student(s) updated.')
        except mysql.connector.Error as err:
            print('hata:', err) 


    def editTeacher(self, teacher: Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print('Database connection closed!')
    