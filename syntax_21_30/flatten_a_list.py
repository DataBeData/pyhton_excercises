#Flatten a Nested List
#You are given a list of lists. 
# #Create one flat list containing all elements.
# Example: [[1, 2], [3, 4]] → [1, 2, 3, 4]


nested_list = [[1, 2], [3, 4]]
united = [x for y in nested_list for x in y]
#print(*united)

flat = []
for y in nested_list:
    for x in y:
        flat.append(x)

crazy_nested =[[[1, 2], [3, 4], [5,6]],[[7,8], [9,10], [11, 12]]]
untangled = [x for y in crazy_nested for z in y for x in z ]
print(*untangled)