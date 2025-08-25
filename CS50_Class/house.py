name = input("what's your name? ")

match name:
    case "Harry" | "hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who")

