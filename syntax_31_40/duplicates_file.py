#Remove Duplicates from File
#Open a text file called emails.txt, 
# and write all unique lines to a new file called unique_emails.txt.
'''
with open("emails.txt", "r", newline="") as file,\
    open("unique_emails.txt", "w", newline="")as new_file:
    inter = set()
    for row in file:
        inter.add(row)
    new_file.writelines(inter)
'''

seen = set()
with open("emails.txt", "r", newline="") as file, \
     open("unique_emails.txt", "w", newline="") as new_file:
    for row in file:
        email = row.strip()
        if email and email not in seen:
            seen.add(email)
            new_file.write(email + "\n")
