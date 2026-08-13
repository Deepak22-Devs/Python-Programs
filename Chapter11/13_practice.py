class vector:
    def __init__(self , i, j ,k):
        self.i = i 
        self.j = j
        self.k = k
    def __add__(self, other):
        result = vector(self.i + other.i , self.j + other.j ,self.k+other.k)
        return result

    def __mul__(self, other):
        result = self.i*other.i + self.j *other.j + self.k*other.k
        return result

    def __str__(self):
        return f"Vector({self.i}, {self.j}, {self.k}) "

V1 = vector(1, 2, 3)
V2 = vector(4, 5, 6)
V3 = vector(7, 8, 9)

print(V1 + V2)
print(V3 + V2)

print(V1 * V2)
print(V3 * V2)