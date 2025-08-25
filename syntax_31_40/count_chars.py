#Count Characters in File
#Open a file the_raven.txt and count the total number of characters 
# (including spaces and punctuation).

with open("the_raven.txt", "r", newline="") as file:
    text = file.read()
    body =len([x for x in text if x.isalnum()]) 
    everything =len([x for x in text])   
    print(body)
    print(everything)
