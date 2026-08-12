class Employee:
    a = 1
    @classmethod   #it priotirise to class atrributes instaed of instance attributes
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45
e.show()