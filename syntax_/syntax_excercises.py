# Example content of data.csv:
# Name,Age
# Alice,30
# Bob,25

import csv  


def main():
    with open("data.csv", "r", newline="") as file:
        reader = csv.DictReader(file, fieldnames=["name", "age"])
        next(file) 
        for row in reader:
            print(row["name"])
            
if __name__ == "__main__":
    main()