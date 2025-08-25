def main():

    n = int(input("What's n?: "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "°m-" * i   # return one value at a time, not all the data at once  / yield is returning an iterator
        # ctrl C stops the itterations

if __name__ == "__main__":
    main()