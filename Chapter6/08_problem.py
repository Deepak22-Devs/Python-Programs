marks = int(input("Enter your mark: "))

if( 90 < marks <= 100):
    print("Your grade is Ex")
elif( 80 < marks <= 90):
    print("Your grade is A ")
elif( 70 < marks <= 80):
    print("Your grade is B")
elif( 60 < marks <= 70):
    print("Your grade is C")
elif( 50 <= marks <= 60):
    print("Your grade is D")
elif( 0 <= marks < 50):
    print("Your grade is F")

else:
    print("Invalid mark")