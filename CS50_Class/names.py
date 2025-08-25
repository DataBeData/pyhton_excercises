'''names = []

for _ in range(3):
    names.append(input("what's your name? "))
for name in sorted(names):
    print(f"Hello, {name}", end="; ")          '''

'''name = input("what's your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()'''

# automates close file
'''with open("names.txt", "a") as file:
    file.write(f"{name}\n")'''

# printing the lines in the text and reformatting it by stripping
'''with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello, ", line.rstrip())'''

# quicker way without readingthrough every line first
'''with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())'''

# sorting it
'''names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")'''

#even better and quicker
with open("names.txt","r") as file:
    for line in sorted(file, reverse=True):
        print("hello, ", line.rstrip())
