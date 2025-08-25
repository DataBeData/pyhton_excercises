# Write a Python program that asks the user for a number and checks if it is a prime number.

'''def main():
    number_to_check = int(input("Give me any whole number: "))  # Ask for the input
    if is_it_a_prime(number_to_check):
        print(f"{number_to_check} is a prime number.")
    else:
        print(f"{number_to_check} is not a prime number.")

# Check if the input is a prime number
def is_it_a_prime(n):
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisors up to the square root of n
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    main()  # Run the code'''

def main():
    number_to_check = int(input("Give me any whole number: "))
    print(f"{number_to_check} is a prime number: {is_it_a_prime(number_to_check)}")

# Check if the input is a prime number
def is_it_a_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    main()