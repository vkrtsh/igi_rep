def count_words(text):
    """
        Counts the number of words in a given text.

        Args:
            text (str): The input text.

        Returns:
            int: The number of words in the text.
    """
    words = text.split()
    word_count = len(words)
    return word_count


def find_longest_word(text):
    """
        Finds the longest word in a given text.

        Args:
            text (str): The input text.

        Returns:
            tuple: A tuple containing the longest word and its index in the text.
    """
    words = text.split()
    longest_word = max(words, key=len)
    word_index = words.index(longest_word)
    return longest_word, word_index + 1


def print_even_words(text):
    """
        Prints every even word from the given text.

        Args:
            text (str): The input text.

        Returns:
            None
    """
    words = text.split()
    even_words = [word for index, word in enumerate(words) if (index + 1) % 2 == 0]
    print("Every even word:")
    for word in even_words:
        if word[-1] == ",":
            print(word[:-1])
        else:
            print(word)


def task4():
    """
        Defines the number of words in a line,  finds the longest word and its sequence number, outputs every even word.
    """
    text = ("So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy "
            "and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and "
            "picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.")

    word_count = count_words(text)
    print("Number of words in the text:", word_count)

    longest_word, word_index = find_longest_word(text)
    print("Longest word:", longest_word)
    print("Index of the longest word:", word_index)

    print_even_words(text)
