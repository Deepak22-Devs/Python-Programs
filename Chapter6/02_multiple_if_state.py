a = int(input("Enter your age: "))

# if statement : 1
if(a%2 == 0):
    print("a is even")


# if statement: 2
if(a >= 18):
    print("you are above the age of consent ")
    print("good for you")

elif(a< 0):
    print("You are entering an invalid age: ")

elif(a == 0):
    print("you are entering 0 which is not a valid age ")

else:
    print("You are below the age of consent")

print("Thamks for coming")