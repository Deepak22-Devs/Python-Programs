class employee():
    language = "Python"
    salary = 1200000
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod  #if there no need for self so we can do it by static method
    def greet():
        print("Good morning")       

harry = employee()
harry.language = "JavaScript"
harry.getinfo() #or
# employee.getinfo(harry)
harry.greet()