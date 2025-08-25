#You are given a dictionary with items and prices. 
# Print all items with a price higher than 10.
# Example:
# {"apple": 5, "banana": 12, "orange": 7, "kiwi": 15}

fruits = {"apple": 5, "banana": 12, "orange": 7, "kiwi": 15}
expensive = []
for fruit in fruits:
    price = fruits[fruit] 
    if price > 10:
        expensive.append(price)
print(expensive)
'''
for fruit in fruits:
    if fruits[fruit] > 10:
        print(fruits[fruit])
'''

'''for fruit, price in fruits.items():
    if price > 10:
        print(fruit)


for fruit in fruits:
    for price in fruits.values():
        if fruits[fruit] == price and price > 10:
            print(fruit)'''    
