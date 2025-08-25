#Sum of Digits
#Given a number, calculate the sum of its digits. 
# (e.g., 123 → 1 + 2 + 3 = 6)


the_digit = input("Give a number with at least two digits: ")
gather = [int(d) for d in the_digit]
result = sum(gather)
print(result)

    

