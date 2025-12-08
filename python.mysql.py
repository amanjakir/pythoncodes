from selectors import SelectSelector

import pymysql

connecton = pymysql.connect(host="localhost", user="root", password="admin", database="oneteam")
pointer = connecton.cursor()

def addStudent():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")
    dob = input("Date of birth: ")
    pointer.execute(f"INSERT INTO students(name, age, course, dob) VALUES ('{name}', '{age}', '{course}', '{dob}')")
    connecton.commit()
    print("Student added successfully!")

def viewStudents():
    pointer.execute("SELECT * FROM students")
    details = pointer.fetchall()
    print("id  Name  Age  Course  Date of birth")
    for std in details:
        print(f"{std[0]}    {std[1]}   {std[2]}   {std[3]}   {std[4]} ")

def deleteStudents():
    viewStudents()
    sid = input("Enter student ID to delete: ")
    pointer.execute(f"SELECT * FROM students WHERE id = '{sid}'")
    data = pointer.fetchone()
    if data:
        pointer.execute(f"DELETE FROM students WHERE id = '{sid}'")
        connecton.commit()
        print("Student deleted successfully!")
    else:
        print("Student ID not found!")


while True:
    print("1.Add Student\n2.View students\n3.Delete student\n4.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        addStudent()
    elif choice == 2:
        viewStudents()
    elif choice == 3:
        deleteStudents()
    elif choice == 4:
        break
