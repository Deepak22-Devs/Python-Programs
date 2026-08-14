try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)

finally:   #it will run here but if finally not in function then it will not run
    print("I am inside finally")