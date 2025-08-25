#Remove Short Words
#From a list of words, remove all words shorter than 4 characters.

word_list =["cat", "dog", "house", "bob", "swim", "ladd", "tim", 
            "place", "holder", "min", "max"]
new_list =[]


def remove_short():
    for word in word_list[:]:   #use a shollow copy "[:]"
        if len(word) < 4:
            #new_list.append(word)
            word_list.remove(word)
    print(word_list)

remove_short()
