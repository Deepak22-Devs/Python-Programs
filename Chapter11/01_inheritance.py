class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

# class programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name of the employee is {self.name} and the salary is {self.salary}")
#     def showlanguage(self):
#         print(f"the name is {self.name} and he is good with {self.language} language")

#we dont need so much lines of code instead i can write thses in samll way likw this:

class programmer(Employee):
    company = "ITC Infotech"     #This is inheritant class
    def showlanguage(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

a = Employee()
b = programmer()
print(a.company, b.company)