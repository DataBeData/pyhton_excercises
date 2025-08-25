import csv
import datetime


def main():
    my_account = LoggingAccount()  # here you are instantiating an object from the class

    amount = ask_for_amount()
    my_account.account_transaction(amount)
    latest_id = my_account.transaction_id
    new_id = my_account.make_transaction_id(latest_id)

    # Update the object's transaction info
    my_account._transaction_id = new_id
    my_account._transaction_amount = amount
    my_account._transaction_date = current_date()

    # Now append the new transaction to the CSV
    my_account.update_all_logs()

    print(f"your new balance: {my_account.balance} ")
    print(f"your transaction date: {current_date()} ")
    print(f"your transaction ID: {new_id}")


class LoggingAccount:
    def __init__(self):
        self.filename = "transactions.csv"
        self._balance = 0
        self._transaction_id = 0
        self._transaction_amount = 0
        self._transaction_date = current_date()

        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(
                    file,
                    fieldnames=[
                        "id",
                        "date",
                        "amount",
                        "balance",
                    ],
                )
                for row in reader:
                    try:
                        self._balance = float(row["balance"])
                        self._transaction_id = int(row["id"])
                        self._transaction_amount = float(row["amount"])
                        self._transaction_date = row["date"]
                    except (ValueError, TypeError):
                        continue  # skip bad/corrupt rows

        except FileNotFoundError:
            with open(self.filename, "w", newline="") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["id", "date", "amount", "balance"]
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "id": self._transaction_id,
                        "date": self._transaction_date,
                        "amount": self._transaction_amount,
                        "balance": self._balance,
                    },
                )

    @property
    def balance(self):
        return self._balance

    @property
    def transaction_id(self):
        return self._transaction_id

    @property
    def transaction_amount(self):
        return self._transaction_amount

    @property
    def transaction_date(self):
        return self._transaction_date

    def account_transaction(self, amount: int):
        self._balance = amount + self._balance
        return self._balance

    def make_transaction_id(self, latest_id):
        new_id = int(latest_id) + 1
        return new_id

    def update_all_logs(self):
        with open(self.filename, "a", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["id", "date", "amount", "balance"]
            )
            writer.writerow(
                {
                    "id": self._transaction_id,
                    "date": self.transaction_date,
                    "amount": self._transaction_amount,
                    "balance": self._balance,
                }
            )


def current_date():
    current_time_date = datetime.datetime.now()
    return current_time_date


def ask_for_amount():
    amount = int(input("Give an amount: "))
    return amount


if __name__ == "__main__":
    main()
