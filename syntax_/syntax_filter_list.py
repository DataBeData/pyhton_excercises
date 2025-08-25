# Example: [1, 2, 3, 4, 5, 6]
# Given a list of numbers, print all the even numbers and remove them from the list.

some_list = [1, 2, 3, 4, 5, 6]
new_list = []

def main():
    for e in some_list:
        if e  %2 == 0:
            some_list.remove(e)   
            print(e,end=", ")    
    #print(new_list)
    print(some_list)
main()