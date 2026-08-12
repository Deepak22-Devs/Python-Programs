# with open ("name.txt") as f:
#     f.open()
n = input("Enter your name: ")
with open ("name.txt", "w") as f:
    f.write(n)