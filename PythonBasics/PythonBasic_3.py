def main():
    word = input("Give me a word: ")
    is_palindrome = check_for_palindrome(word)
    if is_palindrome:
        print("Yes, this is a palindrome")
    else:
        print("No, this is not a palindrome")

def check_for_palindrome(evaluate):
    return evaluate == evaluate[::-1]

if __name__ == "__main__":
    main()
