from calculation_module import calculate_result


def calculate_result(operation_function, operand_numbers):
    if operation_function == add_numbers:
        result_addition = calculate_result(add_numbers, operand_numbers)
        return ("Result of addition:", result_addition)
    if operation_function == subtract_numbers:
        result_subtraction = calculate_result(subtract_numbers, operand_numbers)
        return("Result of subtraction:", result_subtraction)
    if operation_function == multiply_numbers:
        result_multiplication = calculate_result(multiply_numbers, operand_numbers)
        return("Result of multiplication:", result_multiplication)
    if operation_function == divide_numbers:
        result_division = calculate_result(divide_numbers, operand_numbers)
        return("Result of division:", result_division)



