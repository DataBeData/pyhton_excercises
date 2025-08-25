#Count Rows
#Open employees.csv and count 
# how many data rows are in the file (excluding the header).
import csv

with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    count = 0
    top_sellers = []

    for row in reader:
        count += 1
        if int(row["Items Sold"]) > 100:
            top_sellers.append(row["Employees"])

    print("The sales persons with sales over 100:\n")
    for idx, name in enumerate(top_sellers, start=1):
        print(f"{idx}. {name}")

print()
print(f"There are {count} sales persons in our company\n")