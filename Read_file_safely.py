import os

# Ask the user to enter the file name
name = input("Enter the file name that you want to read: ")

# Check whether the file exists
check = os.path.exists(name)

# If the file exists, open and read it
if check == True:

    with open(name, "r") as f:

        print(f.read())

# If the file does not exist
else:
    print("File not found. Please check the file name.")