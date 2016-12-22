def count_positives_sum_negatives(arr):
    count = 0
    sum = 0

    for data in arr:
        if data > 0:
            count += 1
        else:
            sum += data
    if len(arr) == 0:
        return []
    else:
        return [count, sum]
