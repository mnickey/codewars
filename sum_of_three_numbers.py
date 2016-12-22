def get_sum(a, b):
    sum = 0
    start, end = min(a, b), max(a, b)
    while (start) <= end:
        sum += start
        start += 1
        return sum
