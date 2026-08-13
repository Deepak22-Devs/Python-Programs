class employee():
    language = "Python"    #This is an class attributes
    salary = 1200000

harry = employee()
harry.name = "Harry"   #This is an instance attributes 
print(harry.name, harry.language, harry.salary)

rohan = employee()
rohan.name = "Rohon Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)
# Here name is instance attribute and salary and lang. are class attributes as they directly belong to the class