class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1
class programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2
class Manager(programmer):
    def __init__(self):    #it calls parent class
        super().__init__()
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a)
# # print(o.b)  # show an error bcz there is no b attribute in employee class  

# p = programmer()
# print(p.a,p.b)

q= Manager()
print(q.a,q.b, q.c)