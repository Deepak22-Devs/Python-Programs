password = "Python123"
count = 0
while True:
    n = input("Enter your password: ")
    count += 1

    if(n == password):
        print("Access Granted")
        break

    elif(count>=3 ):
        print("Account locked")
        break

    else:
        print("Access Denied")
        print(f"{3-count} attempts reamining")


    