#Write List to File
#Write a list of fruits to a file named fruits.txt, 
# one fruit per line.
import csv

my_fruits = ["apple", "kiwi", "orange", "cherry", "pear", "coconut"]

with open("fruits.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["fruits"])
    for row in my_fruits:
        writer.writerows([[row]])
'''
with open("fruits.txt", "w") as file:
    file.write("fruits\n")
    for fruit in my_fruits:
        file.write(fruit + "\n")
'''