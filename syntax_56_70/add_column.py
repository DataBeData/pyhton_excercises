#Add a New Column
#Read students.csv, add a new column called "Passed" where the value is "Yes" 
#if Grade ≥ 60, otherwise "No". Save it as students_updated.csv.

import csv

with open("students.csv", "r", newline="") as file, \
     open("students_updated.csv", "w", newline="") as updated_file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames + ["Passed"]
    writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        grade = int(row["Grade"])
        row["Passed"] = "Yes" if grade >= 70 else "No"
        writer.writerow(row)