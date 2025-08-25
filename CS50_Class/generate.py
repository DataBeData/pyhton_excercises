import random
'''from random import choice'''

coin = random.choice(["heads", "tails"])
#print(coin)

number = random.randint(1,10)
#print(number)

cards = ["jack", "queen", "king", "ace"]
deck_of_cards = random.shuffle(cards)
#this function doesn't return a value it only shuffles in place (cfr. inside the list)
#print(cards)
#for card in cards:
print(" / ".join(cards), end=" ")


