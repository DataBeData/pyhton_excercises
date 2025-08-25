def meow(n: int) -> str: #metioned the return value or '-> None'
    """Meow n times"""
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

# you can use mypy to check the datatype

'''
def meow(n: int) -> None: #metioned the return value
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
'''