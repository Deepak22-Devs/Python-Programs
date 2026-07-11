secret = 35
attempt = 0
while True:
    n = int(input("Enter your Guess number: "))
    attempt += 1

    if (n > secret):
        print("Too high")

    elif(n < secret):
        print("Too low")

    elif(n == secret):
        print("correct!")
        break

print(f"you guess the number in {attempt} attempt")