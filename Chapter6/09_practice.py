marks = int(input("Enter your mark: "))

if( 90 <= marks <= 100):
    print("Your gradae is: Ex ")
elif( 80 <= marks < 90):
    print("Your gradae is: A ")
elif( 70 <= marks < 80):
    print("Your gradae is: B ")
elif( 60 <= marks < 70):
    print("Your gradae is: C ")
elif( 50 <= marks < 60):
    print("Your gradae is: D ")
elif( 33 <= marks < 50):
    print("Your gradae is: E ")
elif( 0 <= marks <33):
    print("Your gradae is: F ")
elif(marks < 0 or marks> 100):
    print("Invalid mark")

