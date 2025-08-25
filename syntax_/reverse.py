# Reverse a String
# Write a function that takes a string 
# and returns it reversed (without using slicing [::-1]).

def main():
    word = input("give a word: ")
    print(reverse_machine(word))

'''
def reverse_machine(word: str) -> str:
    reverse = word[::-1]
    return(reverse)
'''

def reverse_machine(word: str) -> str:
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

main()