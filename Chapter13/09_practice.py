from functools import reduce
a = [111, 1,2,53,625, 65]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,a))