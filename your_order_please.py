def order(sentence):
    # Check for an empty list and return an empty string if found
    if len(sentence) == 0:
        return ""
    words = {}  # create an empty dictionary
    for word in sentence.split():  # Split the sentence into words to loop over
        for letter in word:  # loop over each letter in word
            if letter.isdigit():  # check to see if the letter is a digit
                words[int(letter)] = word  # assign word to words dictionary
    return_list = [words[key] for key in sorted(words.keys())]  # sort the dictionary by key
    return ' '.join(return_list)  # return the join of all elements in return_list
