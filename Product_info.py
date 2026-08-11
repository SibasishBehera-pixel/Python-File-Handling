# Create an empty list to store product details
products = []

# Take details of 3 products from the user
for i in range(3):

    name = input(f"Enter name of product_{i + 1}: ")

    price = input(f"Enter price of product_{i + 1}: ")

    # Store name and price together as a tuple
    products.append((name, price))


# Open products.txt in write mode
with open("products.txt", "w") as f:

    # Write the table 
    f.write("Product Name\tPrice\n")
    f.write("------------------------\n")

    for name, price in products:
        f.write(f"{name}\t\t{price}\n")


# Open products.txt in read mode
with open("products.txt", "r") as f:

    # Read and display the contents of the file
    print(f.read())