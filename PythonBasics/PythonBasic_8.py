
def square(row, figure):
    for _ in range(row):
        print(figure*row)

def rectangle(row, column, figure):
    if column != row:
        for _ in range (row):
            print(figure*column)
    else:
        print("Adjust parameter input. They can't be equal")

def triangle_right_up(row, figure):
    x = 1
    while x < row:
        for _ in range(row):
            print(figure * x)
            x += 1 

def triangle_right_down(row, figure):
    for _ in range(row):
        print(figure * row)
        row -= 1 

def triangle_isosceles_up(row, figure):
    x = 1
    y = 0
    while row >= x:
        for _ in range(row):
            print(row*" " + y*figure + "#" + y*figure + row*" ")
            x += 1
            y += 1
            row -=1

def triangle_isosceles_down(row, figure):
    x = 0
    y = 0
    while row > x:
        for _ in range(row):
            print(y*" " + row*figure + figure + row*figure + y*" ")
            x += 1
            y += 1
            row -=1
    print(y*" " + figure + y*" ")

'''
def triangle_isosceles_down(rows, figure):
    for i in range(rows):
        spaces = i
        width = (rows - i) * 2 - 1
        print(" " * spaces + figure * width)
'''

def cross(row, figure):
    for i in range(row):
        print(row*" " + figure + row*" ")
    for _ in range(1):
        print(figure*row*2 + figure)
    for i in range(row):
        print(row*" " + figure + row*" ")

def X_marks_the_spot(row, figure):
    for i in range(row):
        for j in range(row):
            if i == j or i + j == row - 1:
                print(figure, end="")
            else:
                print(" ", end="")
        print()

def X_marks_the_spot_me(row, figure):
    x = []
    for i in range(row): 
        x.append(figure)
    print(*x)
    for i in range(row):
        x.append(figure)
    print(*x)

def main():
    X_marks_the_spot_me(5,"0")
    #print(dir(list))

'''
methods = [method for method in dir(str) if not method.startswith('__') and callable(getattr(str, method))]
for i, method in enumerate(methods, 1):
    print(f"{i}. {method}")
'''

if __name__ == "__main__":
    main()
    # square(5, "0")
    # rectangle(5, 10, "0")
    # triangle_right_up(5, "0")
    # triangle_right_down(5, "0")
    # triangle_isosceles_up(5, "0")
    # triangle_isosceles_down(5, "0")
    # cross(5, "0")