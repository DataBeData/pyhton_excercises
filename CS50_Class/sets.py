students = [
    {"name": "Hermoine", "house": "Gryff"},
    {"name": "Ron", "house": "Gryff"},
    {"name": "Harry", "house": "Gryff"},
    {"name": "Draco", "house": "Slyth"},
    {"name": "Ruben", "house": "Huffle"}
]

houses = set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)



#this is the other way using lists
'''
houses = [] 
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)
'''