balance = 5000


def login(pin):
    return pin == 1234
pin = int(input("Enter your PIN: "))
if login(pin):
    print("Acess Granted")
else:
    print("Acess Denied")

def menu():
    print("====== ATM MENU ======")
    print("1. check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    return choice 

def check_balance(balance):
    print(f"You Current Balance: {balance}")
    print("Transaction Succesful!")

def deposit(balance):
    balanceN = int(input("Enter money you want to deposit: "))
    balance += balanceN
    print(f"You current balance is {balance}")
    print("Transaction Succesful!")
    return balance

def withdraw(balance):
    balanceN = int(input("Enter money to Withdraw"))
    if balance > balanceN :
        balance -= balanceN
        print(f"You current balance is {balance}")
        print("Transaction Succesful!")
    else:
        print("Insufficient Balance")
    return balance

def exit_program():
    print("Thank you for using our ATM")
    print("have a nice Day!")



while True:
    # login()
    choice = menu()
    if(choice == 1):
        check_balance(balance)

    elif(choice == 2):
        balance = deposit(balance)

    elif(choice == 3):
        balance = withdraw(balance)

    elif(choice == 4):
        break