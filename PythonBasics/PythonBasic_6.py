# Write a Python program that checks if two given strings are anagrams of each other. 
# Two strings are considered anagrams if they contain the same characters 
# in the same frequency, ignoring spaces, punctuation, and capitalization.
# The program should take two strings as input.
# Ignore spaces, punctuation, and capitalization when checking for anagrams.
# Print True if the strings are anagrams, otherwise print False.

import re

def main():
    word_1 = input("Give a word: ").strip().lower()
    word_2 = input("Give the second word: ").strip().lower()
    result = check_anagram(word_1, word_2)
    print(result)

def check_anagram(x, y):
    # Remove spaces and punctuation
    x = re.sub(r'[^a-zA-Z]', '', x)
    y = re.sub(r'[^a-zA-Z]', '', y)
    # Check if sorted characters are the same
    return sorted(x) == sorted(y)

if __name__ == "__main__":
    main()