# Online Store Discount System
purchase = float(input("Enter total purchase amount (NPR): "))
member = input("Are you a loyalty member? (yes/no): ")

discount = 0

# Main discount
if purchase < 1000:
    discount = 0

elif purchase < 5000:
    discount = 0.05

elif purchase < 15000:
    discount = 0.10
