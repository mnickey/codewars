# Counting sheep...


def count_sheeps(array_of_sheeps):
    count = 0
    for sheep in array_of_sheeps:
        if sheep:
            count += 1
    return count
