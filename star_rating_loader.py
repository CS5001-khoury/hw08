"""
Homework: Star Rating Loader
===========================
Course:   CS 5001
Student:  UPDATE
Semester: UPDATE

Handles file loading and saving for star_rating_app.
It is very common to put this code in a separate file
incase future file types are added. (save to pdf, etc)
"""
import sys
from typing import List, Tuple

from .star_rating_utils import convert_string


def load_movies(filename: str) -> List[Tuple[str, float]]:
    """
    Loads movies from a file. Will assume every movie
    is listed as movie,rating with movies on unique lines
    Any other line that doesn't follow the specified format
    will be skipped.

    Args:
        filename (str): name of file to load

    Returns:
        A list contain a tuple of movie name, rating
    """
    movies = []

   # Student TODO

    return movies


def save_movies(filename: str, movies: List[Tuple[str, float]]) -> None:
    """
    Student, you should update this docstring ...

    Args:
        filename:
        movies:

    Returns:

    """
    # Student TODO

