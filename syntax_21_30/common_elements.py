#Find Common Elements
#Given two lists, print the elements that appear in both.
# Example: [1, 2, 3], [2, 3, 4] → [2, 3]

list_a = [1, 2, 3, 4, 6] 
list_b = [2, 3, 4, 5, 6]

for a,b in zip(list_a, list_b):
        if a == b:
            print(f"this pair {a,b} shares the same position")

for x in list_a:
    if x in list_b:
        print(f"{x} are doubles")
