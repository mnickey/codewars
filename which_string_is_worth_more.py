def highest_value(a, b):
    sum_a, sum_b = 0, 0
    for letter in a:
        sum_a += ord(letter)
    for letter in b:
        sum_b += ord(letter)

    if sum_a >= sum_b:
        return a
    else:
        return b
