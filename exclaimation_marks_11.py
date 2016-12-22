def replace_exclamation(s):
    answer = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for item in s:
        if item.lower() in vowels:
            answer += '!'
        else:
            answer += item
    return answer
