#Filter Rows by Value
#Print all rows from sales.csv 
#where the "Amount" column is greater than 1000.
import csv

with open("sales.csv", "r", newline="") as sales_file:
    reader = csv.DictReader(sales_file)
    for row in reader:
        if int(row["Amount"]) > 1000: 
            print(f"{row['Name']} / {row['Region']} / {row['Amount']}")