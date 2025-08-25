#Count Lines in File
#Open a text file named log.txt and 
#count how many lines it contains.



with open("log.txt", "r", newline="") as file:
    line_count = 0
    for row in file:
        line_count += 1

print(line_count)