#Append to File
#Write a Python script that appends a new line of text 
# Hello, file!" to an existing file log.txt.

with open("log.txt", "a", newline="") as file:
    file.write("hello file!\n")

