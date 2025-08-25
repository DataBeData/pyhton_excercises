import json

number = int(input("Enter a number: "))

with open("json_test.js", "a") as f:
    json.dump(number, f)

with open("json_test.js", "r") as f:
    data = json.load(f)
    print(data) 

    
