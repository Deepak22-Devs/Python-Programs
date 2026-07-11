n = int(input("Enter your number: "))
original = n
total = 0
while n > 0:
    digit = n%10
    total = total + digit**3
    n = n//10


if(total == original):
    print(" This is Armstrang Number")

else:
    print("This is not a arm strang number")