"""
Homework 07: Document Statistics Builder
===========================
Course:   CS 5001
Student:  NAME

REPLACE WITH YOUR HOMEWORK 07 code

Functions for reading document stats. They all assume a 'document' is
a tuple or list of strings, where each string is a line of the document.

For example:
    ('Hello', 'World') is the document
    Hello
    World


    ('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho')
    An old silent pond...
    A frog jumps into the pond—
    Splash! Silence again.
    - Matsuo Basho

"""

from word_lib import clean_word, count_vowels, is_palindrome


def get_number_lines(lines: tuple) -> int:
    """
    Gets the number of lines in the document.

    Examples:
        >>> get_number_lines(('Hello', 'World'))
        2

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of lines in the document
    """
    return 0


def get_number_words(lines: tuple) -> int:
    """
    Gets the number of words in the document. 
    Note, make sure to clean the words before counting them,
    and an 'empty' word should not be counted.

    Examples:
        >>> get_number_words(('Hello', 'World'))
        2
        >>> get_number_words(('Aloha!', '-', 'World'))
        2

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of words in the document
    """
    return 0

def get_vowel_count(lines: tuple) -> int:
    """
    Gets the number of vowels in the document.

    Examples:
        >>> get_vowel_count(('Hello', 'World'))
        3

        >>> get_vowel_count(('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho'))
        24

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of vowels in the document
    """
    return 0


def get_word_palindromes(lines: tuple) -> int:
    """
    Gets the number of palindromes in the document. Ignores punctuation.

    Examples:
        >>> get_word_palindromes(('Hello', 'World'))
        0

        >>> get_word_palindromes(('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho'))
        1

        >>> get_word_palindromes(('raceCar', 'kayak!', 'sator arepo tenet opera rotas!'))
        3

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of palindromes in the document
    """
    return 0


def get_sentence_palindromes(lines: tuple) -> int:
    """
    Gets the number of palindromes in the document. Ignores punctuation.

    Examples:
        >>> get_sentence_palindromes(('Hello', 'World'))
        0

        >>> get_sentence_palindromes(('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho'))
        0

        >>> get_sentence_palindromes(('A raceCar', 'A kayak!', 'sator arepo tenet opera rotas!'))
        1

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of palindromes in the document
    """
    return 0


if __name__ == "__main__":  # if doctest is not installed, comment out these lines
    import doctest

    doctest.testmod(verbose=True)
