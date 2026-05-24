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

else:
    discount = 0.20

# Apply main discount
discounted_price = purchase - (purchase * discount)

# Loyalty member extra discount
if member.lower() == "yes":
    discounted_price -= discounted_price * 0.05

print("Final payable amount: NPR", round(discounted_price, 2))
