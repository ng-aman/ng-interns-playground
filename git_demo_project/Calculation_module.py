# calculation_module.py

def calculate_result(operation_function, numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = operation_function(result, num)

    return result
