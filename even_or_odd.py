# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
from nose.tools import assert_equals


def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


assert_equals(even_or_odd(2), 'Even')
assert_equals(even_or_odd(0), "Even")
assert_equals(even_or_odd(7), "Odd")
assert_equals(even_or_odd(1), "Odd")
