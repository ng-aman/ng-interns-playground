# below function performes division of first number with second number

def divide_numbers(numbers):
    result = numbers[0]
    for i in numbers[1:]:
        result = result/i
    return result
print(divide_numbers([2,3,4,5]))