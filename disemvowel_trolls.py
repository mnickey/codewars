def disemvowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    string = ''.join([l for l in string if l not in vowels])
    return string
