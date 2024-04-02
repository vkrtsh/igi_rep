from checking import check_input
from generator import generate_int_sequence


def generate_numbers_from_user():
    """
        Generates a list of numbers based on user input.

        Yields:
            generator: A generator that yields each number entered by the user.
    """
    size = check_input("Enter the size of the list: ", 1, 50, int)
    for i in range(size):
        number = check_input(f"Enter element {i+1}: ", -50, 50, float)
        yield number


def process_list(numbers):
    """
        Processes a list of numbers and calculates the sum of negative elements
        and the product of elements between the maximum and minimum values.

        Args:
            numbers (list): The list of numbers to process.

        Returns:
            tuple: A tuple containing the sum of negative elements
            and the product of elements between the maximum and minimum values.
    """
    negative_sum = 0
    product = 1

    # Find the maximum and minimum values in the list
    max_value = max(numbers)
    min_value = min(numbers)
    max_index = numbers.index(max_value)
    min_index = numbers.index(min_value)

    # Find the sum of negative elements and the product of elements between the maximum and minimum values
    for num in numbers:
        if num < 0:
            negative_sum += num

    if min_index < max_index:
        for num in numbers[min_index + 1:max_index]:
            product *= num
    elif min_index > max_index:
        for num in numbers[max_index + 1:min_index]:
            product *= num
    elif min_index == max_index:
        product = 0

    return negative_sum, product


def logger(func):
    """
        Decorator function that logs the calling and finishing of a function.

        Args:
            func: The function to be decorated.

        Returns:
            The decorated function.
    """
    def wrapper():
        print("Calling function:", func.__name__)
        func()
        print("Function", func.__name__, "finished")

    return wrapper


@logger
def task5():
    """
        Searches for the sum of the negative elements of the list
        and the product of the elements located between the maximum and minimum elements.
    """
    choice = check_input("Enter '1' for keyboard input or '2' for random number generation: ", 1, 2, int)

    if choice == 1:
        numbers = list(generate_numbers_from_user())
        print(numbers)
    else:
        numbers = generate_int_sequence(check_input("Enter the size of the list: ", 1, 50, int))

    # Process the list and get the results
    negative_sum, product = process_list(numbers)

    # Output the results
    print("List of elements:", numbers)
    print("Sum of negative elements:", negative_sum)
    print("Product of elements between the maximum and minimum values:", product)
