n = int(input("How many students are there: "))

class_total = 0
pass_count = 0
fail_count = 0
highest_percentage = 0
highest_student = ""

for i in range(1, n + 1):
    print(f"\nStudent {i}")

    name = input("Enter your name: ")
    english = int(input("Enter your English mark: "))
    math = int(input("Enter your Math mark: "))
    science = int(input("Enter your Science mark: "))

    total = english + math + science
    percentage = (total / 300) * 100

    # Result and Grade
    if percentage >= 90:
        result = "Pass"
        grade = "Ex"
    elif percentage >= 80:
        result = "Pass"
        grade = "A"
    elif percentage >= 70:
        result = "Pass"
        grade = "B"
    elif percentage >= 60:
        result = "Pass"
        grade = "C"
    elif percentage >= 50:
        result = "Pass"
        grade = "D"
    elif percentage >= 33:
        result = "Pass"
        grade = "E"
    else:
        result = "Fail"
        grade = "F"

    # Count Pass and Fail
    if result == "Pass":
        pass_count += 1
    else:
        fail_count += 1

    # Class Total
    class_total += total

    # Highest Percentage
    if percentage > highest_percentage:
        highest_percentage = percentage
        highest_student = name

    # Student Report
    print("\n----- Student Report -----")
    print("Name:", name)
    print("Total:", total)
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)
    print("Result:", result)

# Class Report
class_average = (class_total / (n * 300)) * 100

print("\n========== CLASS REPORT ==========")
print(f"Class Total Marks: {class_total}")
print(f"Class Average Percentage: {class_average:.2f}%")
print(f"Passed Students: {pass_count}")
print(f"Failed Students: {fail_count}")
print(f"Highest Percentage: {highest_percentage:.2f}%")
print(f"Topper: {highest_student}")