class Account:
    def __init__(self):
        self._balance = 0     # _ meaning it's private

    @property                   # this is now a sort of global variable , accessable?
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        self._balance -= amount

def main():
    account = Account()
    print("Balance = ", account.balance)
    account.deposit(100)
    print("Balance = ", account.balance)
    account.withdraw(50)
    print("Balance = ", account.balance)

if __name__ == "__main__":
    main()  