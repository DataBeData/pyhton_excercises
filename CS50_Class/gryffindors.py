students = [
    {"name": "Hermoine", "house": "Gryff"},
    {"name": "Ron", "house": "Gryff"},
    {"name": "Harry", "house": "Gryff"},
    {"name": "Draco", "house": "Slyth"},
    {"name": "Ruben", "house": "Huffle"}
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryff" #list comprehension!!!!
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)