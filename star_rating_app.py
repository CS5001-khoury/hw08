"""
Homework: Star Rating App
===========================
Student:  UPDATE
Semester: UPDATE

An application that queries the client for movie titles
and a rating for each movie.
"""
from typing import List, Tuple
from .star_rating_utils import clean_title, get_valid_number, convert_rating, convert_string
from .star_rating_loader import load_movies, save_movies

_MIN_STARS = 1
_MAX_STARS = 5
_SPACER = 2


def get_movie(val: str = '') -> Tuple[str, float]:
    """
    Gets a movie and rating from the client.
    if not input is provided, get_movie_by_input()
    is called with its values returned.

    For Example:
        >>> get_movie("v,5")
        ('V', 5)
        >>> get_movie("Princess bride  ,10")
        ('Princess Bride', 10)
        >>> get_movie("   JurAssic shARk  ,    1  ")
        ('Jurassic Shark', 1)

        assume avatar and 3 are entered
        >>> get_movie()              # doctest: +NORMALIZE_WHITESPACE
        Enter a movie:
        Enter a rating 1-5:
        ('Avatar', 3)


    Returns:
        Tuple[str, float]: Movie and float rating
    """
    if val:
        try:
            movie, rating = convert_string(val)
        except ValueError as a:
            print(f"Invalid movie,rating combination: {a}")
            return None
    else:
        movie, rating = get_movie_by_input()
    return movie, rating


def get_movie_by_input() -> Tuple[str, float]:
    """Gets a movie by input, first asking for the movie
    than the rating. Uses get_valid_number to confirm
    rating is a number

    Returns:
        Tuple[str, float]: moving title, rating
    """
    movie = clean_title(input("Enter a movie: "))
    rating = get_valid_number(f"Enter a rating {_MIN_STARS}-{_MAX_STARS}: ")
    return movie, rating


def print_movies(movies: List[Tuple[str, float]]) -> None:
    """Prints out a list of movies.

    prints out the movies to the console along with star ratings.

    Args:
        movies (List[Tuple[str, float]]): A list of movies
    """
    for movie, rating in movies:
        print(f"{convert_rating(rating, _MIN_STARS, _MAX_STARS):<{_MAX_STARS + _SPACER}}{movie}")


def menu() -> Tuple[str, str]:
    """prompts the client for their command.

    Options include: Add, List, Exit, or the Movie,Rating

    Returns:
        Tuple[str, str]: lowercase value, and original value of response
    """
    check = input("""What would you like to do? """)
    return check.strip().casefold(), check


def run() -> None:
    """
    Runs the star rating application.
    """
    movies = load_movies("movie_ratings.txt")
    command, raw = menu()
    while command != "exit":
        if command.find(',') > 0:
            tpl = get_movie(raw)
            if tpl:
                movies.append(tpl)
        elif command == "add":
            movies.append(get_movie())
        elif command == "list":
            print_movies(movies)
        else:
            print("Invalid command: must be add, list, exit, 'movie,rating'.")
        command, raw = menu()
    save_movies("movie_ratings.txt", movies)


if __name__ == "__main__":
    run()
