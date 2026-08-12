class Employee:
    a = 1
    @classmethod  
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.mname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.mname = value.split(" ")[1]
        self.lname = value.split(" ")[2]

e = Employee()
e.a = 45

e.name = "Deepak Kumar Behera"
print(e.fname ,e.mname, e.lname)
print(e.name)
e.show()