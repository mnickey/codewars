def is_opposite(s1, s2):
    answer = ""
    if len(s1) == 0:
        return False
    else:
        for letter in s1:
            if letter.islower():
                answer += letter.upper()
            else:
                answer += letter.lower()

    if answer == s2:
        return True
    else:
        return False
