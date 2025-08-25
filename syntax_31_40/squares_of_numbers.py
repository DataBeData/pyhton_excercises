#Print Squares of Numbers
#Given a list of numbers, 
#Print the square of each number on a new line.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 73]

def square_machine():
    for num in my_list:
            result = num*num
            print(result)
        

square_machine()
