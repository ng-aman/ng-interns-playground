def subtract_numbers(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result