from nose.tools import assert_equals


def repeater(string, n):
    sentence = '"{}" repeated {} times is: "{}"'.format(string, n, string * n)
    return sentence


assert_equals(repeater('yo', 3), '"yo" repeated 3 times is: "yoyoyo"')
assert_equals(repeater('WuB', 6), '"WuB" repeated 6 times is: "WuBWuBWuBWuBWuBWuB"')
assert_equals(repeater('code, eat, code, sleep... ', 2),
              '"code, eat, code, sleep... " repeated 2 times is: "code, eat, code, sleep... code, eat, code, sleep... "')
