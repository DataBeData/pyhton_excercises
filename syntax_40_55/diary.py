#Print Line Numbers
#Open diary.txt and print each line 
# prefixed with its line number (starting at 1).
# Example output:
# 1: Dear diary, today I...


with open("diary.txt") as file:
    for line in file:
        line = enumerate(file, 1)
        for num, sentence in line:
            print(num, sentence, end="")