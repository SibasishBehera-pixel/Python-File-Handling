# Appending below prices inside the file same as in previous task 

with open ('sales_data.txt','a') as f:
    f.writelines('5000\n')
    f.writelines('2500\n')
    f.writelines('1700\n')

# after apennding, Opening the file again to read  updated file 
with open("sales_data.txt", "r") as f:

    datas = f.read()

    print(datas)