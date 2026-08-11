sales = [1200, 450, 980, 1500, 3000]

# Write sales data to the file
with open("sales_data.txt", "w") as f:
    for data in sales:
        f.write(str(data) + "\n")


# Read sales data from the file
with open("sales_data.txt", "r") as f:
    datas = f.read()
    print(datas)