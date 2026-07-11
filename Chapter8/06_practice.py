def convert(f):
    return 5*(f-32)/9

f = int(input("Enter tempreature in F: "))
c = convert(f)
print(f"Tempreature in Celcius = {round(c,2)}°C")