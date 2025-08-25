# Sum of Two Numbers
# Write a program that asks the user for two numbers and prints their sum.
"""
number1 = int(input("Give me a number: "))
number2 = int(input("Give me another number: "))


def SumMaker():
    print(number1 + number2)


SumMaker()
"""
# Simple Calculator
# Ask the user for two numbers and an operator (+, -, *, /). Perform the operation and print the result.

"""
number1 = int(input("Give me a number: "))
number2 = int(input("Give me another number: "))
operatorChoice = input("Choose between: +, -, / or *: ")


def Calculator():
    if operatorChoice == "+":
        print(number1 + number2)
    elif operatorChoice == "-":
        print(number1 - number2)
    elif operatorChoice == "/":
        print(number1 / number2)
    else:
        print(number1 * number2)


Calculator()

"""

# Reverse a String
# Ask the user for a word and print it backwards.

"""
word = input("Give a word: ")


def BackwardsWords():
    print(word[::-1])


BackwardsWords()
"""

# Find the Largest Number
# Ask the user for three numbers and print the largest one.
"""
numbers = input("Give three numbers, seperated by spaces: ")
numbers_list = [int(n) for n in numbers.split()]
largest = max(numbers_list)
print(f"{largest} is the largest number")
"""

# Count Vowels
# Ask the user for a string and print how many vowels (a, e, i, o, u) it contains.
vowel_list = ["a", "e", "i", "o", "u"]
vowelcounter = 0
sentence = input("Give me a 3 word sentence: ")
for n in sentence:
    if n in vowel_list:
        vowelcounter += 1
vowels = vowelcounter
print(f"the amount of vowels are: {vowels}")
