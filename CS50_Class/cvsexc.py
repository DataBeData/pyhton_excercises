import sys

from csv import writer
from csv import reader
from csv import DictReader

name = input("What's your name? ")
print(f"Hello, {name}!")
home = input("Where do you live? ")
print(f"{home} seems like a nice place to live!, \n")

with open("excfile.csv", "a", newline='') as file:
    csv_writer = writer(file)
    csv_writer.writerow([name, home,])

print("Here's an overview of everybody who enrolled! \n")

with open("excfile.csv", "r") as file:
    csv_reader = DictReader(file)
    for row in sorted(csv_reader, key=lambda row: row["homes"]):
        print(f"{row['names']} lives in {row['homes']}")

print()

print("Hope that clarifies things for you.")

print()
