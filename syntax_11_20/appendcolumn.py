# Append Column to CSV
# Open a CSV file people.csv, and add a new column "Country" 
# with the value "Netherlands" for each row. 
# Save it to a new file updated_people.csv.

import csv

with open("people.csv", "r", newline="") as file_OG, open("people_update.csv", "w", newline="") as file_NEW:
    reader = csv.DictReader(file_OG, fieldnames=["Names"])
    next(file_OG)
    writer = csv.DictWriter(file_NEW, fieldnames=["Names", "Country"])
    writer.writeheader()
    for row in reader:
        row["Country"] = "Netherlands"
        writer.writerow(row)     

