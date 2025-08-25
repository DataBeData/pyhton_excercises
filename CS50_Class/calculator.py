'''x = float(input("what is x? "))
y = float(input("what is y? "))

z = round(x/y, 2)

print(f"{z:.2f}")'''

def main():
    x = int(input("what is x? "))
    print("x squared is", square(x))

def square(n):
    return n * n 

if __name__ == "__main__":
    main() 