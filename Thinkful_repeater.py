from nose.tools import assert_equals


def repeater(string, n):
    return string * n


assert_equals(repeater('a', 5), 'aaaaa')
assert_equals(repeater('Na', 16), 'NaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNa')
assert_equals(repeater('Wub ', 6), 'Wub Wub Wub Wub Wub Wub ')
