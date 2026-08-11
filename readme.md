# 🐍 Python File Handling Practice

## 📌 Project Description

This project contains a collection of **Python file-handling practice programs** created to understand and practice working with files in Python.

The programs cover important concepts such as **reading files, writing files, appending data, converting file data, calculating sales statistics, storing product information, checking whether a file exists, and generating discount reports**.

These programs were created as part of Python programming practice.

---

## 📂 Programs Included

### 1. Write and Read Sales Data

This program stores a list of sales values in a text file and then reads the data from the file.

**Concepts Used:**

* Lists
* `open()`
* Write mode (`"w"`)
* Read mode (`"r"`)
* `write()`
* `read()`
* `with` statement

**File Created:**

```text
sales_data.txt
```

---

### 2. Using `read()`, `readline()` and `readlines()`

This program demonstrates three different methods for reading data from a file:

* `read()` – Reads the complete file.
* `readline()` – Reads one line at a time.
* `readlines()` – Reads all lines and returns them as a list.


**Concepts Used:**

* `read()`
* `readline()`
* `readlines()`
* `seek()`
* Lists
* Type conversion
* Loops

---

### 3. Append Sales Data to a File

This program adds new sales values to an existing file without deleting the previous data.


**Concepts Used:**

* Append mode (`"a"`)
* `writelines()`
* File reading
* File updating

**File Used:**

```text
sales_data.txt
```

---

### 4. Sales Data Analysis

This program reads sales data from a text file, converts the values into integers, and calculates:

* **Total Sales**
* **Highest Sales**
* **Lowest Sales**
* **Average Sales**

**Concepts Used:**

* File handling
* `splitlines()`
* Lists
* `int()`
* `sum()`
* `max()`
* `min()`
* `len()`

**Example calculations:**

```text
Total Sales
Highest Sales
Lowest Sales
Average Sales
```

---

### 5. Product Details File

This program accepts the name and price of **three products** from the user and stores the information in a text file.

The product information is stored using tuples.

**Concepts Used:**

* Lists
* Tuples
* `input()`
* `for` loop
* File writing
* File reading
* `write()`

**File Created:**

```text
products.txt
```

---

### 6. Check Whether a File Exists

This program asks the user for a file name and checks whether the file exists before trying to open it.

The `os.path.exists()` function is used for checking the file.

**Concepts Used:**

* `os` module
* `os.path.exists()`
* Conditional statements
* File handling
* Error/message handling

**Example:**

```text
Enter the file name that you want to read: products.txt
```

If the file exists, its contents are displayed.

Otherwise:

```text
File not found. Please check the file name.
```

---

### 7. Product Discount Report

This program stores product names and their original prices in a dictionary.

The user enters a discount percentage, and the program calculates the discounted price for every product.

A **dictionary comprehension** is used to create the discounted price dictionary.

The final report is saved to a text file.

**Concepts Used:**

* Dictionaries
* Dictionary comprehension
* `.items()`
* User input
* Arithmetic operations
* File writing
* File reading
* `with open()`

**File Created:**

```text
discount_report.txt
```

---

## 📚 Python Concepts Practiced

Through these programs, the following Python concepts were practiced:

* Variables
* Lists
* Tuples
* Dictionaries
* Loops
* Conditional statements
* User input
* Type conversion
* File handling
* `open()`
* `with open()`
* File modes:

  * `"r"` – Read
  * `"w"` – Write
  * `"a"` – Append
* `read()`
* `readline()`
* `readlines()`
* `write()`
* `writelines()`
* `seek()`
* `splitlines()`
* `sum()`
* `max()`
* `min()`
* `len()`
* Dictionary comprehension
* `os.path.exists()`

---

## 📁 Files Used

```text
Python File Handling Project/
    1.  Sales_record.py
    2.  Read_files_diffrednt_ways.py
    3.  Append.py
    4.  Summery_Report.py
    5.  Product_info.py
    6.  Read_file_safely.py
    7.  Export_discounted_price.py
```

---

## 🎯 Learning Objectives

The main objectives of this project are:

1. Understand how to create and open files in Python.
2. Learn how to read data from text files.
3. Learn how to write data into files.
4. Understand append mode.
5. Practice different file-reading methods.
6. Convert file data from strings into integers.
7. Perform calculations on data stored in files.
8. Store structured information using lists, tuples, and dictionaries.
9. Check whether a file exists before reading it.
10. Generate simple reports using Python and text files.

---

## 🛠️ Requirements

To run these programs, you need:

* **Python 3.x**
* Any Python editor or IDE, such as:

  * VS Code
  * IDLE
  * PyCharm
  * Jupyter Notebook

No external Python libraries are required for these programs.

---

## ▶️ How to Run

1. Install Python 3.x.
2. Open the project folder in your preferred code editor.
3. Make sure the required `.txt` files are in the correct folder.
4. Run the Python program.
5. Enter the requested information in the terminal.
6. Check the generated `.txt` files for the output.

For example:

```bash
python filename.py
```

---

## 👨‍💻 Author

**Sibasish Behera**

Python Programming Practice Project
