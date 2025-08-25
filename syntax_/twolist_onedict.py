#Create a Dictionary from Two Lists
#You are given two lists: one with names and one with scores. 
# Create a dictionary where each name maps to the score.

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
combined = dict(zip(names, scores))
print(combined)
