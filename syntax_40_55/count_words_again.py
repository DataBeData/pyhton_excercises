#Count Words in File
#Open article.txt and count the total number of words in the file.

with open("article.txt", "r", newline="") as file:
    text = file.read()
    characters = len(text)
    words = [x for x in text.split(" ")]
    
    
    print(len(words), characters)
