from nose.tools import assert_equals


def binary_array_to_number(arr):
    i = 0
    n = len(arr) - 1
    num = 0
    while n >= 0:
        num += arr[n] * pow(2, i)
        i += 1
        n -= 1
    return num


assert_equals(binary_array_to_number([0, 0, 0, 1]), 1)
assert_equals(binary_array_to_number([0, 0, 1, 0]), 2)
assert_equals(binary_array_to_number([1, 1, 1, 1]), 15)
assert_equals(binary_array_to_number([0, 1, 1, 0]), 6)

binary_array_to_number([1, 1, 1, 1])
binary_array_to_number([0, 1, 1, 0])
