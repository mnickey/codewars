from nose.tools import assert_equals


def area_code(text):
    begin = text.index('(')
    return text[begin + 1] + text[begin + 2] + text[begin + 3]


area_code("The supplier's phone number is (555) 867-5309")
assert_equals(area_code("The supplier's phone number is (555) 867-5309"), '555')
assert_equals(area_code("Grae's cell number used to be (123) 456-7890"), '123')
assert_equals(area_code("The 102nd district court's fax line is (124) 816-3264"), '124')
