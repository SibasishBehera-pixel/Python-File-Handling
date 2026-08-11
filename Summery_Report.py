# openning the file in read mode 

with open("sales_data.txt", "r") as f:

    datas = f.read()

    print(datas)

    lists = [] # List for storing sales value 

    # read each line from the file 

    for items in datas.splitlines():

        value = int(items) # converting each sales value from string to integer
        lists.append(value)

 
Total_sales = sum(lists)# Calculate the total sales

print(f"Total sales : {Total_sales}")

Highest_sales = max(lists)# Calculate the highest sales

print(f"Highest sales : {Highest_sales}")

Lowest_sales = min(lists)# Calculate the lowest sales

print(f"Lowest sales : {Lowest_sales}")

Average_sales = sum(lists)/len(lists)# Calculate the average sales

print(f"Average sales : {Average_sales}")
