def find_needle(haystack):
    value = haystack.index('needle')
    return 'found the needle at position {}'.format(value)

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
