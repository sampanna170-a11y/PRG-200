# ATM Withdrawal Validator
balance = float(input("Enter current account balance (NPR): "))
daily_withdrawn = float(input("Enter total amount already withdrawn today (NPR): "))
amount = float(input("Enter withdrawal amount (NPR): "))

daily_limit = 50000

if amount % 500 != 0:
    print("Invalid amount. Must be a multiple of NPR 500.")

elif amount > balance:
    print("Insufficient balance.")

elif daily_withdrawn + amount > daily_limit:
    print("Daily withdrawal limit reached.")