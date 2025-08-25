#Count Even and Odd Numbers
#Given a list of integers, 
# count how many are even and how many are odd, 
# and print the counts.

from random import randint

mixed_bag = [randint(1,100) for i in range(20)]
even = [i for i in mixed_bag if i % 2 == 0]
odd = [i for i in mixed_bag if i % 2 != 0]

'''
for i in range(20):
        numbs = randint(1,100)
        mixed_bag.append(numbs)

for i in mixed_bag:
        if i % 2  == 0:
            even.append(i)
        else:
            odd.append(i)

amount_odd = len(odd)
amount_even = len(even)

'''
print(mixed_bag)
print(odd)
print(even)
print(f"there are {len(odd)} odd numbers, and {len(even)} even numbers")



        