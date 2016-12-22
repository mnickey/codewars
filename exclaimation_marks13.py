from nose.tools import assert_equals


def product(s):
    exclaim_marks = s.count('!')
    q_marks = s.count('?')
    return exclaim_marks * q_marks


assert_equals(product(''), 0)
assert_equals(product('!'), 0)
assert_equals(product('!!??!!'), 8)
