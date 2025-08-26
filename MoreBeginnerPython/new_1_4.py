# Find the Minimum
# Ask the user for several numbers separated by spaces
# and print the smallest number.

"""
while True:
    numbers = input("Give several numbers, seperated by spaces: ")

    if "," in numbers:
        print("Please use spaces, not commas, to separate numbers.")
        continue
    elif " 0 " in numbers:
        print("The Number zero is not allowed, try again")
        continue

    try:
        number_list = [int(n) for n in numbers.split()]
        result = min(number_list)
        print(f"{result} is the lowest number")
        break

    except ValueError:
        print("Please, make sure you input interger numbers")
"""
# Remove Duplicates
# Ask the user for a list of numbers separated by spaces
# and print the list with duplicates removed.

"""
inputNumbers = input("Give several numbers, seperated by spaces: ")

numbersList = [int(n) for n in inputNumbers.split()]

newList = []

def DuplicateCheck():
    for n in numbersList:
        if n not in newList:
            newList.append(n)


DuplicateCheck()
print(sorted(newList))

"""
"""
while True:
    numbersInput = input("Give me 5 numbers, separated by spaces: ")

    if "," in numbersInput:
        print("Error: Please use spaces, not commas, to separate numbers.")
        continue

    split_numbers = numbersInput.split()
    if len(split_numbers) != 5:
        print("Error: Please enter exactly 5 numbers.")
        continue

    if " 0 " in split_numbers:
        print("Error: The number zero is not allowed.")
        continue

    try:
        numbersList = [int(n) for n in split_numbers]
    except ValueError:
        print("Error: Please enter only integer numbers.")
        continue

    print(sorted(set(numbersList)))
    break
"""

# Character Frequency
# Ask the user for a string and print how many times each character appears.

"""

inputString = input("Give me a word: ")


def FrequencyCheck(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


result = FrequencyCheck(inputString)
print(result)

"""

# Fibonacci Sequence
# Ask the user for a number n
# and print the first n numbers in the Fibonacci sequence.

# Password Strength Checker
# Ask the user for a password
# and print whether it is strong (at least 8 characters, contains a number,
# and a special character).
