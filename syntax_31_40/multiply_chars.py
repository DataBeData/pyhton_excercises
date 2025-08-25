#Multiply Each Character
#Ask the user for a string and a number. 
# Print the string with each character repeated that number of times.
# Example: "abc", 3 → "aaabbbccc"

def main():
    while True:
        try:
            word = str(input("give me a word or some random letters: "))
            coefficient = int(input("give me a whole, positive number: "))
            break
        except ValueError:
            print("Please enter a valid input: try again")
    
    result = multiplier_machine(word, coefficient)
    print("".join(result))

def multiplier_machine(word, coefficient):
    empty =[]
    for x in word:
        outcome = x * coefficient
        empty.append(outcome)
    return empty
    
if __name__ == "__main__":
    main()

