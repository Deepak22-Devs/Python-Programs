try:
    a = int(input("Enter your number: "))

except ZeroDivisionError as Z:
    print("Heyy")
    print(Z)
except TypeError as T:
    print("Heyy")
    print(T)
except Exception as s:
    print("Heyy")
    print(s)  