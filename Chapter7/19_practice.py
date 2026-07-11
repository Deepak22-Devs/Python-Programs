n = int(input("Enter your number: "))
i = 0
first = 0
second = 1
# next = first + second
print(first)
print(second)
# print(next)

for i in range ( 0, n-1):
    next = first + second
    print(next)
    first = second
    second = next 