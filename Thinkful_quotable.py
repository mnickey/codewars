from nose.tools import assert_equals


def quotable(name, quote):
    sentence = '{} said: "{}"'.format(name, quote)
    return sentence


assert_equals(quotable('Grae', 'Practice makes perfect'), 'Grae said: "Practice makes perfect"')
assert_equals(quotable('Dan', 'Get back to work, Grae'), 'Dan said: "Get back to work, Grae"')
assert_equals(quotable('Alex', 'Python is great fun'), 'Alex said: "Python is great fun"')
assert_equals(quotable('Bethany', 'Yes, way more fun than R'), 'Bethany said: "Yes, way more fun than R"')
assert_equals(quotable('Darrell', 'What the heck is this thing?'), 'Darrell said: "What the heck is this thing?"')
