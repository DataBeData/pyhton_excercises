import csv
import os

class Bank:
    def __init__(self, filename="global_bankaccount.csv"):
        self.filename = filename
        self._balance = 0
        # Try to read the balance from the CSV file
        if os.path.exists(self.filename):
            with open(self.filename, "r", newline="") as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                row = next(reader, None)
                if row:
                    self._balance = int(row[0])

    def deposit(self, amount):
        self._balance += amount
        self._save_balance()
        return self._balance

    def withdraw(self, amount):
        self._balance -= amount
        self._save_balance()
        return self._balance

    def _save_balance(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["balance"])
            writer.writerow([self._balance])

def main():
    my_account = Bank()

    Q = input("Do you want to deposit? Y / N: ")
    if Q == "Y":
        amount = int(input("How much do you want to deposit?: "))
        new_balance = my_account.deposit(amount)
    elif Q == "N":
        amount = int(input("How much do you want to withdraw?: "))
        new_balance = my_account.withdraw(amount)
    else:
        print("Invalid input.")
        return

    print("Balance =", new_balance, "dollars")

if __name__ == "__main__":
    main()