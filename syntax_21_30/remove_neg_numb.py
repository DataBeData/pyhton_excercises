#Remove Negative Numbers
#From a list of numbers, 
# remove all negative values

from operator import neg


numbers = [1, -2, 3, -4 , 5, -6, 7 , -8, 9, -10]



def neg_remover(numbers):
    pos_numb = []
    for numb in numbers:
        if numb >= 0:
            pos_numb.append(numb)
    return pos_numb

result = neg_remover(numbers)
print(*result)


'''def neg_remover(nums):
    pos_numb =[]
    for numb in nums:
        if numb >= 0:
            pos_numb.append(numb)
    return pos_numb
        
result = neg_remover(numbers)
print(result)'''

