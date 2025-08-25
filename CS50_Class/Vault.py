
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons  #"how do you want the values to be remembered as?, so the parameter galleons as variable self.galleon"
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles and {self.knuts} knuts"
    
    def __add__(self,other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 25)
print(potter)

weasly = Vault(10,5,20)
print(weasly)

ruben = Vault (1000,1,0)
print(ruben)

total = potter + weasly + ruben
print(total)
'''
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons  #"how do you want the values to be remembered as?, so the parameter galleons as variable self.galleon"
        self.sickles = sickles
        self.knuts = knuts
    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles and {self.knuts} knuts"

potter = Vault(100, 50, 25)
print(potter)

weasly = Vault(10,5,20)
print(weasly)

galleons = potter.galleons + weasly.galleons
sickles = potter.sickles + weasly.sickles
knuts = potter.knuts + weasly.knuts

total = Vault(galleons, sickles, knuts)
print(total)
'''