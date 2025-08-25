'''
def main():
    yell("This is CS50")

def yell(phrase):
    print(phrase.upper())
    '''
"""
def main():
    yell(["This", "is", "CS50"])

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
        #print(uppercased)
    print(*uppercased) # it unpacks the python syntax???, 
"""
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased) 

if __name__ == "__main__":
    main()