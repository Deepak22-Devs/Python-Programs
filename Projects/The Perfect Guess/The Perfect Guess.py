
def playgame():
    import random
    d = random.randint(1, 100)
    guess_count = 0
    while True:
        n = int(input("Enter your Guess Number Between 1 to 100: "))
        guess_count = guess_count + 1
        if n<1 or n>100:
            print("Invalid Choice")
        elif d < n :
            print("Too High")
            print("Try again")
        elif d > n :
            print("Too Low")
            print("Try again")
        else:
            print("CORRECT")
            print("END GAME")
            break
    return guess_count
results = playgame()
print(f"You have Guessed  in {results} counts")
while True:
    print("Do you want to try again? ")
    print("1. Yes")
    print("2. No")
    a = int(input("Enter your choice: "))
    if a == 1:
        results = playgame()
        print(f"You have Guessed in {results} counts")
    elif a == 2:
        break
    else:
        print("Invalid Choice!")
