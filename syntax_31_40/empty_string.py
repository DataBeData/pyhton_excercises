#Remove Empty Strings
#You are given a list of strings. 
# Remove all elements that are empty or contain only whitespace.


my_list = ["love", " ", "is", "all", "", "around", 
           "and", "", "", "in", "the", " ", "air"]
"""my_new_list = []
for x in my_list:
    if x.strip():
        my_new_list.append(x)"""

my_new_list =[x for x in my_list if x.strip()]
        
print(*my_new_list)

