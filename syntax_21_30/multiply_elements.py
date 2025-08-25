#Multiply List Elements
#Given a list of numbers, 
# multiply each number by 10 and store the result in a new list.

basic = [15, 2, 34, 4, 54, 6, 74, 87, 19, 10]

mult_10 = [x*10 for x in basic]
print(sorted(mult_10))