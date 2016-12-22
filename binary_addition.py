from nose.tools import assert_equals


def add_binary(a, b):
    sum = a + b
    binary_sum = ('{0:b}'.format(sum))
    return str(binary_sum)


add_binary(1, 1)
add_binary(0, 1)
add_binary(1, 0)
add_binary(2, 2)
add_binary(51, 12)

assert_equals(add_binary(1,1),"10")
assert_equals(add_binary(0,1),"1")
assert_equals(add_binary(1,0),"1")
assert_equals(add_binary(2,2),"100")
assert_equals(add_binary(51,12),"111111")