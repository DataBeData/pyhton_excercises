import csv

students = []

'''with open("students_homes.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name":name, "home":home}
        students.append(student)'''

'''with open("students_homes.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")'''

#now your code is more robust because it doesn't anly depend an the value's place in the row

with open("students_homes.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name":row["name"], "home":row["home"], "house":row["house"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']} and lives in {student['house']}")

