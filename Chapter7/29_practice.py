while True:
    score = 0
    wrong = 0

    # Question 1
    print("\n1. What is the capital of India?")
    print("1. Maharashtra")
    print("2. Delhi")
    print("3. Rajasthan")
    print("4. Gujarat")
    choice = int(input("Enter your choice: "))

    if choice == 2:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! Correct answer is Delhi.")
        wrong += 1

    # Question 2
    print("\n2. What is the capital of Odisha?")
    print("1. Ganjam")
    print("2. Gajapati")
    print("3. Bhubaneswar")
    print("4. Puri")
    choice = int(input("Enter your choice: "))

    if choice == 3:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! Correct answer is Bhubaneswar.")
        wrong += 1

    # Question 3
    print("\n3. In which year did India become independent?")
    print("1. 1947")
    print("2. 1970")
    print("3. 1870")
    print("4. 1980")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! Correct answer is 1947.")
        wrong += 1

    # Question 4
    print("\n4. When do we celebrate Republic Day?")
    print("1. 26-Feb")
    print("2. 26-Jan")
    print("3. 16-Feb")
    print("4. 16-Jan")
    choice = int(input("Enter your choice: "))

    if choice == 2:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! Correct answer is 26-Jan.")
        wrong += 1

    # Question 5
    print("\n5. Which mountain has the highest peak?")
    print("1. Mount Everest")
    print("2. Kanchenjunga")
    print("3. Mount Fuji")
    print("4. Aravalli")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! Correct answer is Mount Everest.")
        wrong += 1

    # Question 6
    print("\n6. When was Mahatma Gandhi born?")
    print("1. 2-Oct")
    print("2. 2-Nov")
    print("3. 2-Dec")
    print("4. 2-Sept")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! Correct answer is 2-Oct.")
        wrong += 1

    # Result
    percentage = (score / 6) * 100

    print("\n==========================")
    print("       QUIZ RESULT")
    print("==========================")
    print(f"Correct Answers : {score}")
    print(f"Wrong Answers   : {wrong}")
    print(f"Percentage      : {percentage:.2f}%")

    if percentage >= 50:
        print("Result          : PASS")
    else:
        print("Result          : FAIL")

    print("==========================")

    # Play Again
    print("\nDo you want to play again?")
    print("1. Yes")
    print("2. No")

    choice = int(input("Enter your choice: "))

    if choice == 2:
        print("Thank you for playing!")
        break