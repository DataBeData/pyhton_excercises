import csv

class BankAccount:
    def __init__(self, filename="bankaccount.csv"):
        self.filename = filename # this is an instance attribute named 'filename'
        self._balance = 0
        try:
            with open(self.filename, "r", newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self._balance = float(row["balance"])
                    break  # Only read the first row
        except (FileNotFoundError, KeyError, ValueError):
            self._balance = 0  # Default if file or value is missing

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._save_balance()

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._save_balance()
        else:
            print("Insufficient funds or invalid amount.")

    def _save_balance(self):
        with open(self.filename, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["balance"])
            writer.writeheader()
            writer.writerow({"balance": self._balance})

# Example usage:
my_account = BankAccount()
print("Current balance:", my_account.balance)
my_account.deposit(50)
print("After deposit:", my_account.balance)
my_account.withdraw(20)
print("After withdrawal:", my_account.balance)