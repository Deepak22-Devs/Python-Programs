def pattern(n):
    if(n ==0):
        return
    print("*"*n)
    pattern(n-1)

# pattern(5)

n = int(input("Enter your nnumber: "))
print(pattern(5))