import math


def task1(x, eps):
    """
    Calculates the value of a function using a power series expansion.

    Args:
        x (float): The input value.
        eps (float): The desired accuracy.

    Returns:
        decimal: The value of the function.
    """

    # Check if the value of x is less than or equal to 1
    if abs(x) <= 1:
        return

    # Initialize variables
    n = 0
    series_sum = 0
    max_iterations = 500

    # Calculate the power series expansion and Set the number of digits
    while True:
        term = round(2 / ((2 * n + 1) * (x ** (2 * n + 1))), abs(int(f'{eps:e}'.split('e')[-1])))
        series_sum += term
        n += 1

        # Check if the desired accuracy is reached or maximum iterations are exceeded
        if n >= max_iterations:
            break

    # Calculate the value of the function using the math module
    math_value = math.log((x + 1) / (x - 1))

    # Print the results
    print(f"Value of x: {x}")
    print(f"Number of terms: {n}")
    print(f"Value of F(x): {round(series_sum, abs(int(f'{eps:e}'.split('e')[-1])))}")
    print(f"Math F(x): {math_value}")
    print(f"Value of eps: {eps}")


# Test the function with x = 2 and eps = 0.000001
