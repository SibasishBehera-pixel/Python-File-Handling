with open("sales_data.txt", "r") as f:

    # ==================== read() ====================

    datas = f.read()

    print("Reading files using .read()")
    print(datas)


    # ==================== readline() ====================

    f.seek(0)

    first_line = f.readline()

    print("Reading files using .readline()")
    print(first_line)


    # ==================== readlines() ====================

    f.seek(0)

    lines = f.readlines()

    print("Reading files using .readlines()")
    print(lines)


    # ==================== Convert strings to integers ====================

    lists = []

    for items in lines:
        value = int(items)
        lists.append(value)

    print("Converted list:")
    print(lists)
