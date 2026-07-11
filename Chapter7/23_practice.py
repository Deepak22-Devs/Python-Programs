n = int(input("Enter your number: "))

for i in range (1, n+1):
    print(" "*(n-i), "*"*(2*i-1), " "*(n-i), sep = "")

print("")
