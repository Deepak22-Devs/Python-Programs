with open ("old.txt") as f:
    content1 = f.read()
with open ("renamed_by_python.txt","w") as f:
    content1 = f.write(content1)