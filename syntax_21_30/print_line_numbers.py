#Print Lines with Line Numbers
#Open a text file quotes.txt and 
# print each line prefixed by its line number (starting at 1).
# Example: 1: First quote

with open("quotes.txt", "r", newline="") as file:
    for x, row in enumerate(file,1):
        print(x, row.strip())
        
