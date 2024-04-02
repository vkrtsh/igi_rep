def find_uppercase_letters(prompt):
    """
        Finds and returns a list of uppercase letters in a given string.

        Args:
        string (str): The input string to search for uppercase letters.

        Returns:
        list: A list of uppercase letters found in the string.
    """
    uppercase_letters = []
    for char in prompt:
        if 65 <= ord(char) <= 90:
            uppercase_letters.append(char)
    return uppercase_letters


def task3():
    """
        Prompts the user to input a string, finds the uppercase letters in the string,
        and prints the count of uppercase letters.

        Returns:
        None
    """
    try:
        string = input("Input string: ")
        if len(string) <= 1000:
            print("The number of uppercase English letters:", len(find_uppercase_letters(string)))
        else:
            print("Input string is too long. The maximum number of characters is 1000.")
    except Exception as e:
        print("An error occurred:", str(e))
