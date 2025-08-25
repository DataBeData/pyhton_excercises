# Exercise:
# Write a Python program that asks the user for their name and age,
# then prints a message saying how old they will be in 10 years.

"""
name = input("What's your name?")
age = int(input("What's your age?"))
future_age = age + 10

print(f"Hello {name}! In ten years you'll be {future_age}.")
"""

# Exercise:
# Write a Python program that asks the user for a number
# and prints whether the number is even or odd.

number = int(input("Give me a number: "))


def NumberCheck():
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is not even number")


NumberCheck()
