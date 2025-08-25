#Filter CSV Rows by Value
#Open grades.csv, and print only 
# the rows where the "Grade" column is greater than 70.

import csv

with open("grades.csv", "r", newline="") as file:
    reader = csv.DictReader(file, fieldnames=["names","grades"])
    next(file)
    for row in reader:
        grade = int(row["grades"])
        if grade > 70:
            print(f"{row['names']}: {row['grades']} %")