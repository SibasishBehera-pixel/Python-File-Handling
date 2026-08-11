# Store product names and their original prices

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000,
}


# Ask the user to enter the discount percentage
discount = int(input("Enter discount in percentage: "))


# Calculate the discounted price for each product
# Dictionary comprehension is used to create a new dictionary
discounted_prices = {
    product: price - (price * discount / 100)
    for product, price in prices.items()
}


# Open the file in write mode
with open("discount_report.txt", "w") as f:

    # Write the table 
    f.write("Product\tOriginal_Price\tDiscounted_Price\n")
    f.write("-------------------------------------------\n")

    # Write each product's details into the file
    for product, price in prices.items():
        f.write(
            f"{product}\t\t{price}\t\t{discounted_prices[product]}\n"
        )


# Open the file in read mode
with open("discount_report.txt", "r") as f:

    print(f.read())