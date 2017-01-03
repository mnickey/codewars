# Remove duplicates from list


def distinct(seq):
    arr = []
    for item in seq:
        if item not in arr:
            arr.append(item)
    return arr
