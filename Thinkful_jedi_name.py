from nose.tools import assert_equals


def greet_jedi(first, last):
    name = last[:3].capitalize() + first[:2].capitalize()
    greet = 'Greetings, master {}'.format(name)
    return greet


greet_jedi('Beyonce', 'knowles')

assert_equals(greet_jedi('Beyonce', 'Knowles'), 'Greetings, master KnoBe')
assert_equals(greet_jedi('Chris', 'Angelico'), 'Greetings, master AngCh')
assert_equals(greet_jedi('grae', 'drake'), 'Greetings, master DraGr')
