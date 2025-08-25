def main():
        choice_made = make_you_choice()
        result = choice_operator(choice_made)
        print(f"The result is: {result}")

number1 = int(input("Give me a number: "))
number2 = int(input("A second number: "))

print()

def make_you_choice():
        the_choice = input(
                "What operator do you want to use?\n" 
                "sum?: choose a\n"
                "difference?: choose b\n"
                "product?: choose c\n"
                "division?: choose d\n\n"
                "Choose your letter: "
                )
        return the_choice

def sum():
        return number1 + number2

def difference():
        return number1 - number2

def product():
        return number1 * number2

def division():
        if number2 != 0:
                return number1 / number2
        else:
                return "Error: Division by zero"

def choice_operator(choice):
        if choice == "a":
                return sum()
        elif choice == "b":
                return difference()
        elif choice == "c":
                return product()
        elif choice == "d":
                return division()
        else:
                return "Invalid choice"
        
if __name__ == "__main__":
        main()