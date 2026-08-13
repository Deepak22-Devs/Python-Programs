class vector:
    def __init__(self , i):
        self.i = i 


    def __len__(self):
        return len(self.i)

#Test the implementation
V1 = vector([1, 2, 3])
print(len(V1))
