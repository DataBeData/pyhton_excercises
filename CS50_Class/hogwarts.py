'''students =["Hermoine", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherine"]'''

'''for student in students:
    print(student)'''

'''for i in range(len(students)):
    print(i + 1,students[i])'''
'''
students = {"Hermoine": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin",
            }
#print(students["Hermoine"]

for student in students:
    print(student, students[student], sep=", lives in ")'''

students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
    ]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")