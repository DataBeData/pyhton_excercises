#Extract Emails from File
#Read a file contacts.txt and print all words that contain the "@" symbol.
'''
with open("contacts.txt") as file:
    contact_list =[]
    for line in file:
        contact_list.append(line)
    for item in contact_list:
        if "@" in item:
            print(item, end="")

# Extract Emails from File
# Read a file contacts.txt and print all words that contain the "@" symbol.

with open("contacts.txt") as file:
    for line in file:
        for word in line.split():
            if "@" in word:
                print(word)
'''
# thi only works if there is only one string, meaning no other words on the line.
with open("contacts.txt") as file:
    for line in file:
        if "@" in line:
            print(line, end="")
