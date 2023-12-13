from addition_module import add_numbers
from subtraction_module import subtract_numbers
from multiplication_module import multiply_numbers
from division_module import divide_numbers
from calculation_module import calculate_result


def main():
    # List of numbers to perform calculations on
    operand_numbers = [2, 3, 4, 5]

    # Perform calculations using the calculate_result function
    result_addition = calculate_result(add_numbers, operand_numbers)
    result_multiplication = calculate_result(multiply_numbers, operand_numbers)
    result_subtraction = calculate_result(subtract_numbers, operand_numbers)
    result_division = calculate_result(divide_numbers, operand_numbers)

    # Display the results
    print("Result of addition:", result_addition)
    print("Result of multiplication:", result_multiplication)
    print("Result of subtraction:", result_subtraction)
    print("Result of division:", result_division)


if __name__ == "__main__":
    # Run the program if it is the main module
    main()
