#Count Vowels
#Write a function that takes a string and 
# counts how many vowels (a, e, i, o, u) it contains.

word = input("give me a word: ")

def vowel_counter(word: str):
    vowels = ["a", "e", "i", "o" ,"u"]
    vowel_container = []
    for x in vowels:
        for vowel in word:
            if vowel == x:
                vowel_container.append(vowel)         
    print(f"there are {len(vowel_container)} vowels in your word")
    print(f"the vowels are: {vowel_container}")
    unique =[]
    for x in vowel_container:
        if x not in unique:
            unique.append(x)
    print(f"the unique vowels are:{unique} ")

vowel_counter(word)
