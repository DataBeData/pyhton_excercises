#Read and Print Lines
#Open a file called notes.txt 
#and print each line that contains the word "important".

import csv
from random import choice

my_choices = ["important", "useless", "something"]
mixture = [choice(my_choices) for _ in range(20)]

def main():
    try:
        with open("notes.txt", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            count = 0
            for row in reader:
                if row == ["important"]:
                    count += 1
                    print(*row)
            print(count)

    except FileNotFoundError:
        with open("notes.txt", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Status"])
            writer.writerows([word] for word in mixture)
        main()

main()