def main():

    n = int(input("What's n?: "))
    for s in sheep(n):
        print(s)
    
    #for i in range(n):
        #print("°m-" * i) 
        #print(sheep(i))

def sheep(n):
    #return "°m-" *n    
    flock = []
    for i in range(n):
        flock.append("°m-" * i)
    return flock


if __name__ == "__main__":
    main()