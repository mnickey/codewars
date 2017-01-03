def digitize(n):
    my_list = []
    digits = str(n)
    for digit in digits:
        my_list.insert(0, int(digit))
    return my_list
