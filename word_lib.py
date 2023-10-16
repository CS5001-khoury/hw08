"""
Homework 07: Library of Word Functions, all written recursively
===========================
Course:   CS 5001
Student:  Your Name

REPLACE with you version of 07

Various functions to practice recursion.
"""


def is_palindrome(word: str) -> bool:
    """
    Recursively looks at a string to determine if it is a palindrome.

    Does not remove punctuation or spaces, and assumes the word is
    already in lower case.

    Examples:
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('hello')
        False

    Args:
        word (str): the word to check

    Returns:
        bool: True if the word is a palindrome, False otherwise
    """
    return True


def count_vowels(word: str) -> int:
    """
    Recursively counts the number of vowels in a string.

    Examples:
        >>> count_vowels('hello')
        2
        >>> count_vowels('aeiou')
        5

    Args:
        word (str): the word to check

    Returns:
        int: the number of vowels in the word
    """
    return 0


def clean_word(word: str) -> str:
    """
    Recursively removes punctuation from a word, and reduces it to lower case.

    Examples:
        >>> clean_word('Hello!')
        'hello'
        >>> clean_word('World...')
        'world'
        >>> clean_word('Aloha, World!')
        'alohaworld'

    See:
        https://docs.python.org/3/library/stdtypes.html#str.isalnum


    Args:
        word (str): the word to remove punctuation from

    Returns:
        str: the word without punctuation
    """
    return ''


if __name__ == "__main__":  # if doctest is not installed, comment out these lines
    import doctest

    doctest.testmod(verbose=True)
