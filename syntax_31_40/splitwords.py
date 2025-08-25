#Split and Count Words
#Ask the user to input a sentence. 
# Split it into words and print how many words it contains.

def main():
    sentence = input("give any sentence: ")
    sentence_splitter(sentence)


def sentence_splitter(sentence):
    word_list = sentence.split(" ")
    num_of_words = len(word_list)
    print(f"the sentence has {num_of_words} words")


if __name__ == "__main__":
    main()