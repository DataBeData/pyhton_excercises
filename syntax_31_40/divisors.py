#List All Divisors
#Write a function that takes an integer 
# and returns a list of its divisors.
# Example: 12 → [1, 2, 3, 4, 6, 12]


def main():
    while True:
        number = input("Give me an integer: ")
        try:
            divisors_machine(number)
            break
        except ValueError:
            print("Please enter a valid interger")
           
def divisors_machine(number):
    new_number = int(number)
    divisor_list =[]
    for x in range(1, new_number):   
        if new_number % x == 0:
            divisor_list.append(x)
    divisor_list.append(new_number)
    print(divisor_list)

"""def main():
    while True:
        number = input("Give me an integer: ")
        try:
            number = int(number)
            divisors = divisors_machine(number)
            print(divisors)
            break
        except ValueError:
            print("Please enter a valid integer.")

def divisors_machine(number):
    return [x for x in range(1, number + 1) if number % x == 0]

if __name__ == "__main__":
    main()"""



if __name__ == "__main__":
    main()