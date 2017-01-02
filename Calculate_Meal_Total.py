def calculate_total(subtotal, tax, tip):
    amount = (subtotal + (subtotal * tip) / 100)
    tax = subtotal * tax / 100
    return float("%.2f" % (amount + tax))
