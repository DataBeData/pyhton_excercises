def main():
    name = input("what's your name? ")
    print(hello(name))

def hello(to="world"):
    '''print("hello,", to)'''
    return f"hello, {to}"

if __name__ == "__ main__":
    main()