import sys

import csv

#get user input
first = input("What's your first name? ")
last = input("what's your last name? ")

print()

#make or define the column headers
complete_name = ["first name", "last name"]

#open the file in append mode for a dictionary
with open("csv2.csv", "a", newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=complete_name)
    csv_writer.writerow({"first name": first, "last name": last})

print("Here's an overview of everybody who enrolled! \n")

#read the file based on a sorted function based on the columns
with open("csv2.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in sorted(csv_reader, key=lambda word: word["last name"][-1]):
        print(f"{row['last name']} {row['first name']}")

print()

print("Hope that clarifies things for you.")

print()

