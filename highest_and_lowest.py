def high_and_low(numbers):
    number_list = [int(num) for num in numbers.split(' ')]
    return '{} {}'.format(max(number_list), min(number_list))