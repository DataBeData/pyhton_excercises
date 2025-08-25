#Open a text file story.txt and count how many times the word "magic" appears.

def main():
    with open("story.txt", "r", errors="ignore", encoding="utf-8") as file:
        content =  file.read()
        tally = content.count("magic")
    print(tally)

main()
