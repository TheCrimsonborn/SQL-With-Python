from DBManager import DbManager
from Student import Student
from datetime import date

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*****\n1-Students List\n2-Add Student\n3-Update Student\n4-Delete Student\n5-Add Teacher\n6-Class Lessons\n7-Exit(E)"
        while True:
            print(msg)
            option = input("Option: ")
            if option == '1':
                self.displayStudents()
            elif option == '2':
                self.addStudent()
            elif option == '3':
                self.editStudent() 
            elif option == '4':
                self.deleteStudent() 
            elif option == 'E':
                break
            else:
                print('Wrong option!')

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input('Student ID: '))

        self.db.deleteStudent(studentid)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input('Student ID: '))

        student = self.db.getStudentById(studentid)

        student[0].name = input('Name:') or student[0].name
        student[0].surname = input('Surname:') or student[0].surname
        student[0].gender = input('Gender (M/F):') or student[0].gender
        student[0].classid = input('Class: ') or student[0].classid

        year = input("Year: ") or student[0].birthdate.year
        month = input("Month: ") or student[0].birthdate.month
        day = input("Day: ") or student[0].birthdate.day

        student[0].birthdate = date(year,month,day)
        self.db.editStudent(student[0]) 


    def addStudent(self):
        self.displayClasses()
        
        classid = int(input('Class: '))
        number = input('Number: ')
        name = input('Name: ')
        surname = input('Surname: ')
        year = int(input('Year: '))
        month = int(input('Month: '))
        day = int(input('Day: '))
        birthdate = date(year,month,day)
        gender = input('Gender (M/F):')

        students = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(students)

    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f'{c.id}: {c.name}')

    def displayStudents(self):       
        self.displayClasses()
        classid = int(input('Class: '))

        students = self.db.getStudentsByClassId(classid)
        print("Students List")
        for std in students:
            print(f'{std.id}-{std.name} {std.surname}')

        return classid



app = App()     
app.initApp()