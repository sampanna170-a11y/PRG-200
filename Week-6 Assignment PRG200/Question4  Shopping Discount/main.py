from discount import final_price, TAX_RATE

products = [
    ("Laptop", 85000, 10),
    ("Headphones", 4500, 15),
    ("Phone Case", 800, 5),
    ("USB Cable", 600, 0)
]

print("Tax Rate =", TAX_RATE)
print()

for item, price, discount in products:
    final = final_price(price, discount)

    print("Product:", item)
    print("Original Price:", price)
    print("Final Price:", round(final, 2))
    print()
    