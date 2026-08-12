class Employee:
    company = "ITC"
    salary = 1200000
    def show(self):
        print(f"The name of the employee is {self.company} and the salary is {self.salary}")

class coder:
    language = "Python"
    def printlanguage(self):
        print(f"Out of all the languages here is your langaughe: {self.language}")

class programmer(Employee, coder):
    company = "ITC Infotech"    
    def showlanguage(self):
        print(f"The name of the employee is {self.company} and the salary is {self.salary}")

a = Employee()
b = programmer()
b.show()
b.printlanguage()
b.showlanguage()
