def check_input(prompt, a, b, name_type):
    """
    Get an  input from the user.

    Args:
    message (str): The message to display to the user.

    Returns:
    name_type: The input from the user.
    """
    while True:
        try:
            value = name_type(input(prompt))
            if name_type == str and a <= len(value) <= b:
                return value
            elif name_type != str and a <= value <= b:
                return value
            else:
                print(f"Invalid input. Please enter a valid {name_type} number between {a} and {b}.")
        except Exception as e:
            print("An error occurred:", str(e))
