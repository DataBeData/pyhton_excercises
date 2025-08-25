#Find the Maximum Value
#Write a function that takes a list of numbers 
# and returns the highest number (without using max()).

numbers = [1, 22, 789, 34, 3, 5, 67, 3, 80]

def max_spitter(numbers: list):
    highest = 0
    for num in numbers:
        if num > highest:
            highest = num
    print(highest)

max_spitter(numbers)