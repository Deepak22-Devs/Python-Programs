import random
computer = random.choice ([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {"s" : -1, "w" : 0 , "g" : 1}
reverseDict = {-1 : "s", 0 : "w", 1 : "g"}
you = youDict[youstr]
print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")
if computer == you:
    print("It's Draw!")
else:
    if computer == -1 and you == 0:
        print("You Loss!")
    elif computer == -1 and you == 1:
        print("You win!")
    elif computer == 1 and you == 0:
        print("You win!")
    elif computer == 1 and you == -1:
        print("You loss")
    elif computer == 0 and you == 1:
        print("You Lose!")
    elif computer == 0 and you == -1:
        print("You Win!")
    else:
        print("Something went wrong!")