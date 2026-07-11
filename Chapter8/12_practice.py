
def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a , b):
    return a * b

def division(a , b):
    if(b == 0): 
        print("Cannot divided by zero.")
    else:
        return a/b

while True:
    print("====== Calculator ======")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        a = int(input("Enter your number: "))
        b = int(input("Enter your number: "))
        print(f"Your addition is {add(a,b)}")
    elif(choice == 2):
        a = int(input("Enter your number: "))
        b = int(input("Enter your number: "))
        print(f"Your substraction is {substract(a,b)}")
    elif(choice == 3):
        a = int(input("Enter your number: "))
        b = int(input("Enter your number: "))
        print(f"Your multiplication is {multiply(a,b)}")
    elif(choice == 4):
        a = int(input("Enter your number: "))
        b = int(input("Enter your number: "))
        print(f"Your division is {division(a,b)}")
    elif(choice == 5):
        break 
    else:
        print("Invalid Choice")

    print("Do another calculation?")
    print("1. yes")
    print("2. No")
    choice = int(input("Enter you choice: "))
    if (choice == 2):
        break
    elif(choice == 1):
        continue
    else:
        print("Invalid choice")
