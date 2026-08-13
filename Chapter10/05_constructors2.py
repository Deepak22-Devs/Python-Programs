class employee():
    language = "Python"
    salary = 1200000
    def __init__(self, name , salary, language):    #it is type of dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("Hello my self Deepak")

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod         #if there no need for self so we can do it by static method
    def greet():
        print("Good morning")       
harry = employee("Harry", 1300000  , "JavaScript")
print(harry.name, harry.salary, harry.language)