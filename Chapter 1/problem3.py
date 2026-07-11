import os

# Get the current directory
directory = "/collections "

# Print the contents of the directory
contents = os.listdir(directory)

print("Contents of the directory:")
for item in contents:
    print(item)