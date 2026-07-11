n = int(input("Enter your number: "))
    

for i in range (1, n+1):
    print(f"Table of {i}")

    for l in range(1 , 11):
        print(f"{i} X {l} = {i*l} ")

print("Done!")