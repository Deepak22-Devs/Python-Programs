student = []

def menu():
    print("===== MENU =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

def add_student():
    name = input("Enter student name: ")
    roll_number = int(input("Enter student Roll Number: "))
    percentage = int(input("Enter student percentage: "))

    if 90 <= percentage <= 100:
        grade = "Ex"
    elif 80 <= percentage < 90:
        grade = "A"
    elif 70 <= percentage < 80:
        grade = "B"
    elif 60 <= percentage < 70:
        grade = "C"
    elif 50 <= percentage < 60:
        grade = "D"
    elif 33 <= percentage < 50:
        grade = "E"
    else:
        grade = "F"

    student.append([name, roll_number, percentage, grade])
    print("Student added successfully.")

def show_student():
    if len(student) == 0:
        print("No students available.")
        return

    print("\nName\t\tRoll No\tPercentage\tGrade")
    print("-" * 50)

    for i in student:
        print(f"{i[0]}\t\t{i[1]}\t{i[2]}\t\t{i[3]}")

def search_student():
    sname = input("Enter student name: ")
    found = False

    for nname in student:
        if sname == nname[0]:
            print("\n====== Student Details ======")
            print(f"Name        : {nname[0]}")
            print(f"Roll Number : {nname[1]}")
            print(f"Percentage  : {nname[2]}")
            print(f"Grade       : {nname[3]}")
            found = True
            break

    if not found:
        print("Student not found.")

def delete_student():
    dname = input("Enter student name: ")
    found = False

    for l in student:
        if dname == l[0]:
            student.remove(l)
            print("Student record deleted successfully.")
            found = True
            break

    if not found:
        print("No student record found.")

while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("How many students do you want to add? "))
        for _ in range(n):
            add_student()

    elif choice == 2:
        show_student()

    elif choice == 3:
        search_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice.")
        