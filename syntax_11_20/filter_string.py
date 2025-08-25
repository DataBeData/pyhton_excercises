#Filter Strings in List
#Given a list that contains strings and integers
#create a new list that only contains the strings.

mixed_bag = [1, 2, 3, "hello", "cat", "dog", 4, 5 , "help"]
new_list =[]
def string_filter():
    for i in mixed_bag:
        if type(i) == str:
            new_list.append(i)

string_filter()
print(new_list)