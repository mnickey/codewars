# Get the mean of an array


def get_average(marks):
    sum = 0
    for mark in marks:
        sum += mark
    return sum / len(marks)
