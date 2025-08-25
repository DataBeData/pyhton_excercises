#Find Words Starting with a Letter
#Given a list of words, print all words 
# that start with the letter "s" (case-insensitive).

random_bag = ["bells", "doors", "sweet", "string", "bow", "suspenders", "weight"]

'''
for word in random_bag:
   if word.startswith("s"):
      print(word)
'''


for word in random_bag:
      if word[0] == "s":
        print(word)

      