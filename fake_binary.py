def fake_bin(x):
    value = ""
    for number in str(x):
        if int(number) < 5:
            value += str(0)
        else:
            value += str(1)
    return value
