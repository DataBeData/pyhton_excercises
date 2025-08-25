import random

# Sum of a List
# Ask the user for several numbers separated by spaces,
# then print the sum of those numbers.
"""
numbers = input("give a few numbers: ")
numbers_list = [int(n) for n in numbers.split()]
sumNumbers = sum(numbers_list)
print(sumNumbers)
"""
# Palindrome Checker
# Ask the user for a word and print whether it is a
# palindrome (reads the same forwards and backwards).

""" 
word = input("Give a word: ")


def PalindromeChecker():
    if word == word[::-1]:
        print("f{word} is a palindrome")
    else:
        print("f{word} is NOT  a palindrome")


PalindromeChecker()
"""

# Multiplication Table
# Ask the user for a number and print its multiplication table up to 10.
"""
table_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = int(input("Give a Number: "))


def Table():
    for n in table_list:
        print(n * number)


Table()
"""

# Word Counter
# Ask the user for a sentence and print how many words it contains.

"""
sentence = input("Give me a sentence:")


def LetterCounter():
    letters = sentence.replace(" ", "")
    counting = len(letters)
    print(counting)


def WordCounter():
    words = sentence.split()
    total = len(words)
    print(total)


LetterCounter()
WordCounter()

"""
# Guess the Number
# Generate a random number between 1 and 10.
# Ask the user to guess the number and tell them if they are correct or not.


def NumberGenerator():
    count = 0
    while True:
        choice = int(input("Choose a number between 1 and 10: "))
        randomNumber = random.randint(1, 10)
        if choice == randomNumber:
            print("You WON")
            break
        else:
            count += 1
            print("You LOST, give it another try")
    print(f"It took you {count +1} tries")


NumberGenerator()
