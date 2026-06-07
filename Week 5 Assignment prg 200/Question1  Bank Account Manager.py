class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds for {self.name}")
        else:
            self.balance -= amount

    def get_balance(self):
        print(f"{self.name} ({self.account_number}) - Balance: NPR {self.balance}")


accounts = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000),
]

bank_accounts = []

for name, account_number, balance in accounts:
    bank_accounts.append(BankAccount(name, account_number, balance))

for account in bank_accounts:
    if account.account_number == "A002":
        account.deposit(3000)

    elif account.account_number == "A003":
        account.withdraw(15000)

    elif account.account_number == "A001":
        account.withdraw(2000)

print("Final Account Balances:")
for account in bank_accounts:
    account.get_balance()

