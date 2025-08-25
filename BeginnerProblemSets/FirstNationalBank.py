import csv


def main():
    my_account = FirstNationalBankAccount()  # here you create an instance of a class
    print(
        f"Your balance: {my_account.balance}"
    )  # calling upon the property to acces the current data
    amount = int(
        input("Give your amount?: ")
    )  # asking for input from the user and assigning it to  variable
    my_account.BankBusiness(amount)  # adding to your instance via a method
    new_balance = my_account.update_account()  # writing your data back into the file
    print(
        f"Your new balance:{new_balance}"
    )  # side effect of printing the update value/data


class FirstNationalBankAccount:
    def __init__(self, filename="FirstNational_StartAccount.csv"):
        self.filename = filename
        self._balance = 0

        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self._balance = int(row["balance"])
                    break

        except Exception:
            with open(self.filename, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["balance"])
                writer.writeheader()
                writer.writerow({"balance": self._balance})

    @property
    def balance(self):
        return self._balance

    def BankBusiness(self, amount: int):
        if amount >= 0:
            self._balance = self._balance + amount
        else:
            self._balance = self._balance + amount
        return self._balance

    def update_account(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["balance"])
            writer.writeheader()
            writer.writerow({"balance": self._balance})
            return self._balance


if __name__ == "__main__":
    main()
