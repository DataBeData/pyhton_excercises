#Create a List from User Input
#Ask the user to enter 5 numbers. 
#Store them in a list and print the list.

def main():
    the_input = input("Give me fve numbers, seperate by a space: ")
    the_list = [int(x) for x in the_input.split()]
    print(the_list)

main()