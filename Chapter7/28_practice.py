password = 1234
count = 0
balance = 5000
while True:
    n = int(input("Enter your pin: "))
    count += 1
    if(n == password):
        while True:
             print("Acess granted!")
             print("======= ATM MENU =======")
             print("1. check balance ")
             print("2. Deposit ")
             print("3. Withdraw ")
             print("4. Exit")
             choice = int(input("Enter your choice number:" ))
             if(choice == 1):
                 print(f"Your balance is {balance}")
                #  break
             elif(choice == 2):
                 new_balance = int(input("Enter money to Deposit: "))
                 balance += new_balance
                 print(f"Transaction Succesful")
                 print(f"Current Balance: {balance}")
                #  break
             elif(choice==3):
                 new_balance = int(input("Enter amunt to Withdraw: "))
                 if(new_balance<balance):
                     balance -= new_balance
                     print(f"Transaction Succesful")
                     print(f"Current Balance: {balance}")
                 else:
                     print("Insufficent balance")
                #  break
             elif(choice == 4):
                 print("Exit!")
                 break
             else:
                 print("Invalid choice!")

        break

    elif(count>=3):
        print("Card is Blocked!")
        break

    else:
        print("Acess Denied")
        print(f"{3-count} Attempts remaining")


