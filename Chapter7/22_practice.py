n = int(input("Enter your number: "))

for i in range (1, n+1):
    print(f" "*(n-i), end=" ")
    print(f"*"*i, end=" ")
    print("")