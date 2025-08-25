#Capitalize Names in a List
#You are given a list of names with lowercase letters. 
# Capitalize the first letter of each name.
# Example: ["alice", "bob", "charlie"] → ["Alice", "Bob", "Charlie"]

names = ["alice", "bob", "charlie"] 

'''
def capitalizer():
  for name in names:
    capital = name.capitalize()
    print(capital)
'''
def capitalizer():
    for name in range(len(names)):
        names[name] = names[name].capitalize()
    print(names)

capitalizer()


