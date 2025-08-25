#read File into List
#Read the file shopping.txt where each line is an item. 
# Store each item in a list and print it.

with open("shopping.txt") as file:
    shoppinglist = []
    for line in file:
        shoppinglist.append(line)
shop_list = enumerate(shoppinglist,1)
for num, item in shop_list:
    print(f"{num}. {item.capitalize()}", end="")