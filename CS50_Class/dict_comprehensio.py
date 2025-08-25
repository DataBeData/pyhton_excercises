students = ["Hermoine", "Harry", "Ron", "Ruben"]

gryffindors = {student:"Gryffindor" for student in students}  

'''
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
'''

'''
gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})
'''

print(gryffindors)