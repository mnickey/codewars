# Digits explosion
# Python

def explode(s):
    exploded = ""
    for letter in s:
        exploded += letter * int(letter)
    return exploded
