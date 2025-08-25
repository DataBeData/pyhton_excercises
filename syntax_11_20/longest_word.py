# Find Longest Word
# You are given a list of words. 
# Print the longest word in the list.

word_list = ["cat", "cats", "catty", "dog", "dogged", "unknowable", "irrepressably"]

# ...existing code...

def long_word_finder():
    longest = "a"
    for word in word_list:
        if len(word) > len(longest):
            longest = word
    print(longest)

long_word_finder()
