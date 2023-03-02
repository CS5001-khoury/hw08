"""
Homework: Star Rating Utils
===========================
Student:  UPDATE
Semester: UPDATE

Utility functions that help with star_rating_app.
Each function should be independent.
"""
import string
from typing import Tuple


def clean_title(movie: str) -> str:
    """
    Cleans a string stripping trailing and leading whitespaces,
    and converts it to title case.

    Examples:
        >>> clean_title("     v")
        'V'
        >>> clean_title("Princess bride  ")
        'Princess Bride'
        >>> clean_title("it's a wonderful life")
        'It's A Wonderful Life'

    See:
        https://docs.python.org/3/library/stdtypes.html#string-methods

    Arguments:
        movie (str): movie title to clean
    Returns:
        str : the movie in title case, and leading and trailing spaces removed
    """
    return string.capwords(movie.strip())


def get_valid_number(prompt: str) -> float:
    """Prompts the user for an int value, and keep
    repeating until a numeric value is entered.


    Args:
        prompt (str): the string to prompt the client with

    Returns:
        float: the final value
    """
    try:
        val = input(prompt)
        f_val = float(val)
    except ValueError:
        print("Please enter a valid number.")
        return get_valid_number(prompt)
    return f_val


def convert_rating(val: float, min_s: int, max_s: int) -> str:
    """Converts rating to stars (*) equal
    to the rating. Will convert any value under min_s to be
    min_s and anything over max_s to be max_s.

    if a float is passed in, the value is rounded down to the
    nearest int

    Args:
        val (float): the rating value
        min_s (int): the minimum number of stars.
        max_s (int): the minimum number of stars.

    Returns:
        str: stars between min_s and max_s
    """
    val = int(val)  # safe to convert as long as it is a float
    if val < min_s:
        val = min_s
    if val > max_s:
        val = max_s
    return "*" * val


def convert_string(line: str) -> Tuple[str, float]:
    """
        Converts a string of format MovieName,Rating
        to a tuple of (MovieName,Rating)

        Raises errors if the format of the line is invalid for
        conversion.
    Args:
        line (str): a string of format MovieName,Number

    Returns:
        Tuple[str, float]: the move with a cleaned title,
                           and a float value of the number
    """
    last = line.rfind(",")  # find the last comma - so movie names can have commas
    if last < 0:
        raise ValueError("Must contain at least one comma")
    movie_s = line[0:last]
    rating_s = line[last+1:]
    movie = clean_title(movie_s.strip())
    try:
        rating = float(rating_s.strip())
    except ValueError:
        raise ValueError("Invalid number value for rating!")  # changes message on raise, allowed!
    return movie, rating
