from nose.tools import assert_equals


def square_digits(num):
    squared = ""
    for digit in str(num):
        squared += str(int(digit)**2)
    return int(squared)

square_digits(9199)
assert_equals(square_digits(9119), 811181)
