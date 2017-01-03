def duty_free(price, discount, holiday_cost):
    count = -1
    savings = 0
    while savings < holiday_cost:
        savings += price * (discount / 100.0)
        count += 1
    return count
