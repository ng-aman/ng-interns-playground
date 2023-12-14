from calculation_module import calculate_result


def calculate_result(operation_function, operand_numbers):
    if operation_function == add_numbers:
        return ("Result of addition:", result_addition)
    if operation_function == subtract_numbers:
        return("Result of subtraction:", result_subtraction)
    if operation_function == multiply_numbers:
        return("Result of multiplication:", result_multiplication)
    if operation_function == divide_numbers:
        return("Result of division:", result_division)



