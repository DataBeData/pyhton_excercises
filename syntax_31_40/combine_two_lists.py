#Combine Two Lists
#You are given two lists of equal length. 
# Combine them into a list of tuples.
# Example: [1, 2], ["a", "b"] → [(1, "a"), (2, "b")]

nums_list = [1, 2, 3]
lett_list = ["a", "b", ]

def main():
    yaya = tupleator()
    print(yaya)
    dada = tupelator_2()
    print(dada)


def tupleator():
    tuple_list =[]
    for x in zip(nums_list, lett_list):
        tuple_list.append(x)
    return tuple_list
 

def tupelator_2():
    version_2 = list(zip(nums_list, lett_list))
    return version_2

if __name__ == "__main__":
    main()

