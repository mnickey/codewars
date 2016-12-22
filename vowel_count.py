def getCount(inputStr):
    return sum(vowel in 'aeiouAEIOU' for vowel in inputStr)