def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("what's n?\n --> input here: "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")


main()