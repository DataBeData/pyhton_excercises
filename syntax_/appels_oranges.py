#Replace all occurrences of "apple" in a list with "orange" and print the updated list.
# first  make a randomizer for the a some fruits an make a list.

import random

mix_fruit = ["apple", "kiwi", "mango", "grapes", "leche", "banana"]
random_fruit = []


def fruit_machine():
    for _ in range(10):
        fruit = random.choice(mix_fruit)
        random_fruit.append(fruit)

    for i in range(len(random_fruit)):
        if random_fruit[i] == "apple":
            random_fruit[i] = "orange"

    print(random_fruit)
    

    
fruit_machine()



