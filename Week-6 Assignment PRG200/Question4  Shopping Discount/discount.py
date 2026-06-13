TAX_RATE = 0.13

def apply_discount(price, percent):
    return price - (price * percent / 100)

def apply_tax(price):
    return price + (price * TAX_RATE)

def final_price(price, discount_pct):
    price_after_discount = apply_discount(price, discount_pct)
    return apply_tax(price_after_discount)
