# Write a Python program that checks if a given string is a palindrome. 
# A palindrome is a word, phrase, or sequence that reads the same backward as forward 
# (ignoring spaces, punctuation, and capitalization).
# Extend the program to handle numeric palindromes 
# (e.g., 121 is a palindrome).
import re

def main():
    the_choice = input("Do you want a 'number'or a 'word?\nYour Choice?: ")
    if the_choice == "word":
         a_string_to_check = input("Give me a sentence: ")
         new_result = cleaned_up(a_string_to_check)
         a_palindrome = palindrome_checker(new_result)
         print(f"{a_string_to_check} is {a_palindrome}")
    
    elif the_choice == "number":
        a_number_to_check = input("Give me a number: ")
        new_result = cleaned_up_number(a_number_to_check)
        a_palindrome = palindrome_checker(new_result)
        print(f"{a_number_to_check} is {a_palindrome}")
    else:
        print("not the correct input; try again")
        main()
        
def cleaned_up(sentence):
    result = sentence.lower()
    new_result = re.sub(r'[^a-z]', '', result)
    return new_result

def cleaned_up_number(number):
    result = re.sub(r'[^0-9]', '', number)
    return result

def palindrome_checker(new_result):
    if new_result == new_result[::-1]:
        return "a palindrome"
    else:
        return "not a palindrome"

'''
if __name__ == "__main__":
    main()
  
import re

def main():
    input_value = input("Enter a word or number to check if it's a palindrome: ").strip()
    
    # Automatically determine if the input is numeric or alphabetic
    if input_value.isdigit():
        cleaned_input = clean_input(input_value, keep="numbers")
    else:
        cleaned_input = clean_input(input_value, keep="letters")
    
    if is_palindrome(cleaned_input):
        print(f"'{input_value}' is a palindrome.")
    else:
        print(f"'{input_value}' is not a palindrome.")

def clean_input(input_string, keep="letters"):
    """
    Cleans the input string by keeping only letters or numbers.
    :param input_string: The string to clean.
    :param keep: "letters" to keep only alphabetic characters, "numbers" to keep only digits.
    :return: A cleaned string.
    """
    if keep == "letters":
        return re.sub(r'[^a-z]', '', input_string.lower())
    elif keep == "numbers":
        return re.sub(r'[^0-9]', '', input_string)
    else:
        raise ValueError("Invalid 'keep' parameter. Use 'letters' or 'numbers'.")

def is_palindrome(cleaned_input):
    """
    Checks if the cleaned input is a palindrome.
    :param cleaned_input: The cleaned string or number to check.
    :return: True if it's a palindrome, False otherwise.
    """
    return cleaned_input == cleaned_input[::-1]

if __name__ == "__main__":
    main()
'''