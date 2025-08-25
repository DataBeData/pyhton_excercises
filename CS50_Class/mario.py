'''print("#")
print("#")
print("#")'''

'''for _ in range(3):
    print("###")'''

'''def main():
    print("#\n" * 3, end="")'''

'''def main():
   print_column(3)

def print_column(height):
   for _ in range(height):
      print("#")'''

'''def main():
     print_row(4)
def print_row(blocks):
    for _ in range(blocks):
        print("?" * blocks + 6*"?")'''

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


main()
