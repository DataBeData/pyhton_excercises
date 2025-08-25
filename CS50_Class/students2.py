students = []

'''with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
for student in sorted(students):
    print(student)'''

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        '''student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)'''
        # same as above but more consise
        student = {"name":name, "house":house}
        students.append(student)

'''def get_name(student):
    return student["name"]
def get_house(student):
    return student["house"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")'''

# more succint

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
