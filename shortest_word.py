from nose.tools import assert_equals


def find_short(s):
    split_words = s.strip().split()
    min_word = len(split_words[0])
    for word in split_words:
        # if len(split_words[len(i)]) < min_word:
        if len(word) < min_word:
            min_word = len(word)
    return min_word


print(find_short("bitcoin take over the world maybe who knows perhaps"))
print(find_short("turns out random test cases are easier than writing out basic ones"))
print(find_short("lets talk about javascript the best language"))
print(find_short("i want to travel the world writing code one day"))
print(find_short("Lets all go on holiday somewhere very cold"))

assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
assert_equals(find_short("lets talk about javascript the best language"), 3)
assert_equals(find_short("i want to travel the world writing code one day"), 1)
assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)
