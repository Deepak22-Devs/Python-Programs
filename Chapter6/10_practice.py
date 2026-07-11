name = input("Enter your name: ")
Roll_no = int(input("Enter your roll number: "))
markE = int(input("Enter your English mark: "))
markM = int(input("Enter your math mark: "))
markS = int(input("Enter your science mark: "))

total = markE + markM + markS
avg = (total/300)*100

if(markE >= 33 and markS >= 33 and markM>=33):
    Result = "Pass"
else:
    Result = "Fail"

if( 90 <= avg <= 100 ):
    grade = "Ex"
elif( 80<= avg <90 ):
    grade = "A"
elif( 70<= avg < 80 ):
    grade = "B"
elif( 60<= avg <70 ):
    grade = "C"
elif(50<= avg <60 ):
    grade = "D"
elif( 33<= avg< 50):
    grade = "E"
elif( avg < 33 ):
    grade = "F"

if(markE>markM and markE > markS):
    highest = "English"
elif(markM>markE and markM > markS):
    highest = "Mathematics"
elif(markS>markE and markS > markM):
    highest = "Science"


print("Name: ",name)
print("Roll no: ",Roll_no)
print("English: ",markE)
print("Mathematics: ",markM)
print("Science: ",markS)
print("Total: ",total)
print(f"Percentage: {avg}%")
print("Highest mark subject: ",highest)

print("Result: ", Result)
print("Grade: ",grade)