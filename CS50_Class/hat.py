import random

class Hat:   
    houses = ["Gryff", "Huffle", "Raven", "Slyth"]
    # this is a 'class variable' / just one copy that others share the same varibale or list,...
    # so no self needed, because these refer to them selves, a specific object
    @classmethod
    def sort(cls,name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry") 

'''
class Hat:    # if there is only one instance it's called a singletons , so no objects, just a container
    def __init__(self):  #only usful if you want ot instanciate a version/object
        self.houses = ["Gryff", "Huffle", "Raven", "Slyth"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))
hat = Hat() # this is the constructor
hat.sort("Harry") 
'''
