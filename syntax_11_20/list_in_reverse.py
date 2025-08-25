#Print List in Reverse
#You are given a list of items. 
# Print them in reverse order using a loop (no [::-1]).

my_list_of_items = ["apple", "butter", "cat", "deer", "eggs", "fever", "giraffe"]
#new_list = my_list_of_items[::-1]
looped_list = []

def reverse_machine():
    for word in my_list_of_items:
        looped_list.append(word)
    spit = sorted(looped_list, reverse=True)
    print(spit)


reverse_machine()