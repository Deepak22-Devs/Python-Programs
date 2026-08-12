class Employee:
    a = 1
class programmer(Employee):
    b = 2
class Manager(programmer):
    c = 3

o = Employee()
print(o.a)
# print(o.b)  # show an error bcz there is no b attribute in employee class  

p = programmer()
print(p.a,p.b)

q= Manager
print(q.a,q.b, q.c)