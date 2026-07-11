def inch_to_cms (inch):
    return inch*2.54

inch = int(input("Enter value in inches: "))
print(f"The corresponding centimeter value is {inch_to_cms (inch)}")