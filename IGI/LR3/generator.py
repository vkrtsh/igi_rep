import random


def generate_random_integer():
    """
    Generates a random sequence of int numbers.

    Yields:
        int: The generated number.
    """
    while True:
        yield random.randint(-50, 50)


def generate_int_sequence(n):
    """
    Generates a sequence of random integers.

    Args:
        n (int, optional): The number of random integers to generate.

    Returns:
        list: List of random integers.
    """
    random_number_generator = generate_random_integer()
    random_number_list = [next(random_number_generator) for _ in range(n)]
    return random_number_list
