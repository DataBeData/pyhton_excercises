# Sum of Digits
# Ask the user for a number and print the sum of its digits.
"""
number = input("Give a number with 3 digits: ")

digits = [int(n) for n in number]
result = sum(digits)

print(result)
"""

# Count Uppercase Letters
# Ask the user for a string and print how many uppercase letters it contains.
"""
inputString = input("Give a sentence: ")
result = sum(1 for i in inputString if i.isupper())
print(result)
"""

# Find the Average
# Ask the user for several numbers separated by spaces and print their average.

numbers = input("Give several numbers, seperated by a space: ")

numberList = [int(n) for n in numbers.split()]

elements = len(numberList)

numberSum = sum(numberList)

result = numberSum / elements

print(result)

# Remove Vowels
# Ask the user for a word and print the word with all vowels removed.

# Find the Longest Word
# Ask the user for a sentence and print the longest word in the sentence.
