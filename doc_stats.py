"""
Homework 08: Document Statistics Program
===========================
Course:   CS 5001
Student:  Your Name

Update this file by adding required functions.

Small program that builds document statistics from a command line input.
"""
import sys

from doc_stats_builder import (
    get_number_lines,
    get_number_words,
    get_sentence_palindromes,
    get_vowel_count,
    get_word_palindromes,
)
from doc_view import get_input, print_stats, read_file, write_json_file

# provided functions
def get_stats_block(doc: tuple) -> tuple:
    """
    Builds a tuple of statistics from a tuple of strings.

    Args:
        doc (tuple): A tuple of strings.

    Returns:
        tuple: A tuple of statistics in the order of lines, words, vowels,
        palindromes and sentence palindromes.
    """
    return (
        get_number_lines(doc),
        get_number_words(doc),
        get_vowel_count(doc),
        get_word_palindromes(doc),
        get_sentence_palindromes(doc),
    )


def check_args_for_help(args: list) -> bool:
    """
    Checks to see if -h is in the args, if so, prints the help message and returns True.

    Args:
        args (list): A list of command line arguments.

    Returns:
        bool: True if -h is in the args, False otherwise.
    """
    if "-h" in args or "--help" in args:
        print_help()
        return True
    return False


def print_help() -> None:
    """
    Prints the help message for the program.
    """
    print("Usage: python doc_stats.py [-h|--help] [-f filename]  [-o filename]")
    print("Options:")
    print("  -f filename: The name of the file to analyze.")
    print("  -h or --help: Print this help message and exit")
    print("  -o filename: The name of the file to write the output to.",  
          "If filename is not provided, but -o is used then the default file", 
          "name is out.txt.")

# end provided functions
# edit the following functions

def get_input_file(args: list) -> str:
    """
    Checks to see if -f file_name is in the args, if so, returns the file name,
    or returns an empty string if it is not there.

    On a bad format, such as -f (nothing) or -f followed by a -- or - (another flag),
    raises a ValueError.

    Args:
        args (list): A list of command line arguments.

    Returns:
        str: The file name if it exists in the args and is valid, otherwise an empty string.
    """
    return "" # replace with your code


def get_output_file(args: list) -> str:
    """
    Checks to see if a -o file_name is in the args, if so returns the file name or
    the empty string if it is not there.

    If -o is provided without a following file name, it uses the default 'out.txt'.

    Args:
        args (list): A list of command line arguments.

    Returns:
        str: A file name if -o is in the args, otherwise an empty string.
    """
    return "" # replace with your code


def main(args) -> None:
    """
    Main function for the program.
    """
    pass # replace with your code


if __name__ == "__main__":
    main(sys.argv)
