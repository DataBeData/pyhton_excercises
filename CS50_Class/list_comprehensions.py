def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]   # this is a list comprehension
    print(*uppercased) 

if __name__ == "__main__":
    main()