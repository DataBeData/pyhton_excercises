students = [
    {"name": "Hermoine", "house": "Gryff"},
    {"name": "Ron", "house": "Gryff"},
    {"name": "Harry", "house": "Gryff"},
    {"name": "Draco", "house": "Slyth"},
    {"name": "Ruben", "house": "Huffle"}
]

def is_gryffindor(s):
    '''
    if s["house"] == "Gryff":
        return True               
    else:
        return False
    ''' 
    return s["house"] == "Gryff"

gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])