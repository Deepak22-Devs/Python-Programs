a1 = int(input("Enter your math mark: "))
a2 = int(input("Enter your Physics mark: "))
a3 = int(input("Enter your Chemistry mark: "))

s = (a1+a2+a3)/3

if(a1>33 and a2>33 and a3>33 and s>40):
    print(f"congrats! you are passed: {s}%")

else:
    print(f"Sorry, you are fail, try again next year: {s}%")
