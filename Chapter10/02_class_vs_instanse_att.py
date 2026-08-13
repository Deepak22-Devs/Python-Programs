class employee():
    language = "Python"
    salary = 1200000

harry = employee()
harry.language = "JavaScript"
print(harry.language, harry.salary)
# here instance attribute have proritty so instance attribute will be choosen
