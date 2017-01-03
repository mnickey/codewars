# Find n'th Digit of a Number


def find_digit(num, nth):
    num = abs(num)
    num = str(num)
    if nth <= 0:
        return -1
    elif nth > len(num):
        return 0
    else:
        return int(num[-nth])
