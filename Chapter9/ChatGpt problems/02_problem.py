count = 0
with open("data.txt","r") as f:
    text= f.read()
    words = text.split()

    for word in words:
        if word.isdigit():
            count += 1
print(count)