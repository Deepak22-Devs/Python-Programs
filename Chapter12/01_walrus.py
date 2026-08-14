#using walrus operator( := ) we can fix 3 line in one line 
if (n := len([1,2,3,4,5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")