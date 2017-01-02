def sum_array(arr):
    if arr is None:
        return 0
    if len(arr) <= 2:
        return 0
    else:
        arr = sorted(arr)
        arr.pop(0)
        arr.pop(-1)
        answer = sum(arr)
        return answer
