class employee():
    language = "Python"
    salary = 1200000
    def __init__(self):    #it is type of dunder method which is automatically called
        print("Hello my self Deepak")
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod         #if there no need for self so we can do it by static method
    def greet():
        print("Good morning")       
harry = employee()
harry.language = "JavaScript"   
harry.getinfo() #or             
# employee.getinfo(harry)       
harry.greet()

rohan = employee()