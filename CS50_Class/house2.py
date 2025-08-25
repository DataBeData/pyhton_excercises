import csv

name = input("what's your name? ")
home = input("Where do you live? ")

'''with open("house2.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])'''

# more concise, using a dictionary van keys and values

with open("house2.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name":name, "home":home})