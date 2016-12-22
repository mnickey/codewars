from nose.tools import assert_equals


def my_min(arr):
    return min(arr)


def my_max(arr):
    return max(arr)


# Test.it("Fixed Min")
assert_equals(min([-52, 56, 30, 29, -54, 0, -110]), -110)
assert_equals(min([42, 54, 65, 87, 0]), 0)
assert_equals(min([1, 2, 3, 4, 5, 10]), 1)
assert_equals(min([-1, -2, -3, -4, -5, -10]), -10)
assert_equals(min([9]), 9)

# Test.it("Fixed Max")
assert_equals(max([-52, 56, 30, 29, -54, 0, -110]), 56)
assert_equals(max([4, 6, 2, 1, 9, 63, -134, 566]), 566)
assert_equals(max([5]), 5)
assert_equals(max([534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555]), 555)
assert_equals(max([9]), 9)
