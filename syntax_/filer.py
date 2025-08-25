#Filter and Append to New List
#From a list of temperatures, 
# select only those greater than 25 degrees and add them to a new list.

temps = [25, 26, 30, 2, -3, 45, 17, 43, 22, 19, 16, 54]
#scorching = [temp for temp in temps if temp > 25]
    
scorching = list(filter((lambda x: x > 25), temps))

scorching = [temp for temp in temps if temp > 25]
print(scorching)


print(scorching)