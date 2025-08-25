# Check for Palindromes
#Given a list of words, 
# print the ones that are palindromes 
# (words that read the same forward and backward).
# Example: ["level", "hello", "radar"] → "level" and "radar"

my_list = ["level", "hello", "radar"]

def palindrome_finder():
       for word in my_list:
              if word == word[::-1]:
                     print(word)
palindrome_finder()