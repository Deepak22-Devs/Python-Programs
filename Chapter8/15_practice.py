student = []

def add_student():
    name = input("Enter student name: ")
    Roll_Number = int(input("Enter student Roll Number: "))
    percentage = int(input("Enter student percentage: "))
    if (90<= percentage <=100):
        Grade = "Ex"
    elif(80<= percentage < 90):
        Grade = "A"
    elif(70<= percentage < 80):
        Grade = "B"
    elif(60<= percentage < 70):
        Grade = "C"
    elif(50<= percentage < 60):
        Grade = "D"
    elif(33<= percentage < 50):
        Grade = "E"
    elif(percentage < 33):
        Grade = "F"

    # return name, Roll_Number, percentage
    student.append([name, Roll_Number, percentage, Grade])
    # student.append(Roll_Number)
    # student.append(percentage)
    # student.append(Grade)

def show_student():
    print(f"name           Roll No.             percentage")
    print(f"----------------------------------------------")
    for i in student:
        print(i)

def search_student():
    sname = input("Enter student name: ")
    found = False
    for nname in student:
        if(sname == nname[0]):
            print(f"====== Student Details =======")
            print(f"name         = {nname[0]}")
            print(f"Roll Number  = {nname[1]}")
            print(f"Percentage   = {nname[2]}")
            print(f"Grade        = {nname[3]}")
            found = True
            break
        if not found:
            print("Student not found")


def delete_student():
    name2 = input("Enter Student name: ")
    for manme in student:
        print("")