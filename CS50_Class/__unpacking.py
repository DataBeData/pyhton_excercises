
#def total(galleons=0, sickles=0, knuts=0):  these are defaults, can avoid errors
def total(galleons:int, sickles:int, knuts:int):
    return (galleons * 17 + sickles ) * 29 + knuts
    #return knuts, galleons, sickles

#coins = [100, 50, 25]   # it always needs to line up with the same amount of arguments
coins = {"galleons": 100, "sickles":50, "knuts": 25}
#coins(galleons=100, sickels=50, knuts=25)

#print(total(coins[0], coins[1], coins[2]), "coins")
#print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "coins")
#print(*total(100,50,25), "coins")
print(total(**coins))
#print(total(knuts=25, galleons=100, sickles=50), "coins")




'''
first, _ = input("What's your name: ").split(" ")
print(f"Hello, {first} ")
'''