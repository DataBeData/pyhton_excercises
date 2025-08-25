#Sum All Integers in a CSV Column
#Open a CSV file numbers.csv 
# and print the sum of all the numbers in the "Value" column.
"""
import csv
adding =[]
with open("numbers.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        result = int(row["value"])
        adding.append(result)

        [int(row["value"]) for row in reader] #list comprehension

print(sum(adding))
"""
import csv

with open("numbers.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    total = sum(int(row["value"]) for row in reader) #generator expression

print(total)