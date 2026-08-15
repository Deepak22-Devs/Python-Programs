def divisibles5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,34233,53,6234235, 65]

f = list(filter(divisibles5,a))
print(f)