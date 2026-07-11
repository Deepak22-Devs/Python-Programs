def sum(n):
    if (n == 1):
        return 1
    return sum(n-1) + n
n = int(input("Enter your number: "))
print(f" sum of {n} numbers is {sum(n)}")