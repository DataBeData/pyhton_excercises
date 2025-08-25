
'''def MakeAList():
    NumberList = [i for i in range(21)]
    NumberList.pop(0)
    print(NumberList)
MakeAList()'''

def lijstjesmetcijfers():
    Strtlijst = [i for i in range(1, 21)]
    Even =[]
    Odd =[]
    for i in Strtlijst:
        if i % 2 == 0:
            i = Even.append(i)
        else: i = Odd.append(i) 
    print(f"Even getallen:{Even}")
    print(f"Oneven getallen:{Odd}")

lijstjesmetcijfers()
     
