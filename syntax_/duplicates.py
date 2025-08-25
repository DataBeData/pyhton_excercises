#Remove Duplicates from List
#Remove duplicates from a list and sort the result in ascending order.
import random

my_list = []

for i in range(20):
    mix = random.randrange(1, 5)
    my_list.append(mix)

unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

unique_list.sort()
print(unique_list)

'''
import random

my_list = []

for i in range(20):
    mix = random.randrange(1, 5)
    my_list.append(mix)

# Remove duplicates and sort
unique_sorted = sorted(set(my_list))

print(unique_sorted)
'''