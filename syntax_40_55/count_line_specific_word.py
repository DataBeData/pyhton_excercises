#Count Lines with Specific Word
#Count how many lines in comments.txt 
#contain the word "error" (case-insensitive).
import string
with open("comments.txt", "r", newline="") as file:
    count = 0
    word = "error"
    for line in file:
        clean_line = [w.strip(string.punctuation) for w in line.split()]
        if word in clean_line:
            count += 1
    print(count)


