import random
import csv

mix_fruit = ["apple", "kiwi", "mango", "grapes", "leche", "banana"]
fruitbowl = []

def random_fruit():
        for _ in range(25):
            mix = random.choice(mix_fruit)
            fruitbowl.append(mix)
        return fruitbowl


def main():
    
    try:
        with open("Fruitmixer.csv", "r", newline="") as file:   
            reader = csv.reader(file)
            fruit_row = list(reader)
        
        updated_bowl =[]
        for row in fruit_row:
            for fruit in row:
                updated_bowl.append("orange" if fruit == "apple" else fruit)
            print(*updated_bowl)

                
    except FileNotFoundError:
        random_fruit()
        with open("Fruitmixer.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(fruitbowl)
            print("File not found. Created a new file and added random fruits.")

main()
