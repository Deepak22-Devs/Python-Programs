def input_student():
    name = input("Enter student name: ")
    English = int(input("Enter English mark: "))
    Odia = int(input("Enter Odia mark: "))
    Math = int(input("Enter Math mark: "))
    Science = int(input("Enter Science mark: "))
    Social_science = int(input("Enter Social_science mark: "))
    total = English+Odia+Math+Science+Social_science
    return name, total
    # name, total = input_student()

def calculate_percentage(total):
    percentage = (total/500)*100
    return percentage
    # percentage = calculate_percentage(total)

def calculate_grade(percentage):
    if(100>= percentage>=90):
        Grade = "Ex"
    elif(90> percentage>=80):
        Grade = "A"
    elif(80> percentage>=70):
        Grade = "B"
    elif(70> percentage>=60):
        Grade = "C"
    elif(60> percentage>=50):
        Grade = "D"
    elif(50> percentage>=33):
        Grade = "E"
    elif(percentage < 33):
        Grade = "F"
    return Grade
    # Grade = calculate_grade(percentage)

def display_result(name , total, percentage, Grade):
    print(f"========== REPORT CARD ==========")
    print(f"Name        : {name}")
    print(f"Total       : {total}")
    print(f"Percentage  : {percentage}")
    print(f"Grade       : {Grade}")
    print(f"=================================")
    
while True:
    # input_student()
    name , total = input_student()
    percentage =  calculate_percentage(total)
    Grade = calculate_grade(percentage)
    display_result(name , total, percentage, Grade)
