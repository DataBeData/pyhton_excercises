import emoji

class Student:
    def __init__(self, name, house=None, patronus=None): #initializes the contents of the object / self let's you store it in the current object that was just created
        if not name:                        # here the None make it optional // self --> so you have acces to the current object
            raise ValueError("Missing name")
        if house not in ["Gryffindor","Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name        # here you create an instance variable/ attribute
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return emoji.emojize(":deer:")  # 🦌
            case "Otter":
                return emoji.emojize(":otter:")  # 🦦
            case "Phoenix":
                return emoji.emojize(":fire:")  # 🔥
            case _:
                return emoji.emojize(":sparkles:")  # ✨
 
def main():
    student = get_student() 
    #print(f"{student.name} from {student.house}")
    print("Expecto Patronum")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House:  ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)
    #student = Student(name, house)  #constructor call; creates a Student object that is structured the same aka BLUE PRINT
                                    #you need to populate it with values/arguments inside with a function that is called
                                    #here you're passing in two things to the function, but you need to be able to STORE IT
                                    #here you're actually constructing it
    '''return student'''


'''
def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student
'''

'''
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name,"house": house}
'''
'''student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student'''
'''name = input("Name: ")
    house = input("House: ")
    return [name, house]'''

if __name__ == "__main__":
    main()
