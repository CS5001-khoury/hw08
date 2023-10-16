"""
Homework 08: Document Statistics
===========================
Course:   CS 5001
Student:  Your Name

NEED TO UPDATE! This time students need to update this file by adding required functions.

It is very common to break the view into a different file. This allows a single spot
to edit client interaction. For example, i could change this file 
to use a GUI instead of the console, and the rest of the program would not need to change.

The "view" for document view.
"""
END_WORD = "STOP"
INPUT_PROMPT = "Enter text to analyze (STOP to end):"
PRINT_TEMPLATE = """
Document Statistics
===================
Number of lines: {}
Number of words: {}
Number of vowels: {}
Number of palindromes: {}
Number of sentence palindromes: {}
"""

# provided code
def print_stats(doc_stats: tuple | list) -> None:
    """
    Prints the document statistics to the console.

    Examples:
        >>> print_stats((1, 2, 3, 4, 5))         # doctest: +NORMALIZE_WHITESPACE
        Document Statistics
        ===================
        Number of lines: 1
        Number of words: 2
        Number of vowels: 3
        Number of palindromes: 4
        Number of sentence palindromes: 5

    Args:
        doc_stats (tuple | list): the document statistics
    """
    print(PRINT_TEMPLATE.format(*doc_stats))


def get_input() -> tuple:
    """
    Gets input from the client until the word STOP is entered on a
    single line in all caps. Each line is added to a list, then the
    tuple is returned. The STOP word is not included in the tuple.

    Examples: (note doctest is not run on this due to input prompt)
       Assume the client enters the following:
       Hello
       World
       STOP
       >> get_input()
       ('Hello', 'World')

       Assume the client enters the following:
       STOP
       >> get_input()
       ()

       Assume the client enters the following:
       An old silent pond...
       A frog jumps into the pond—
       Splash! Silence again.
       - Matsuo Basho
       STOP
       >> get_input()
       ('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho')
    """
    lines = []
    print(INPUT_PROMPT)
    while True:
        line = input().strip()
        if line == END_WORD:
            break
        lines.append(line)
    return tuple(lines)
# end provided code


#student code
def read_file(file_path: str) -> tuple:
    """
    Reads in a file and returns a tuple with each line as a string.
    Each line will have leading and trailing whitespace removed.

    Args:
    file_path (str): The path of the file to be read.

    Returns:
    tuple: A tuple with each line of the file as a string.
    """
    return () # replace with your code


def write_json_file(doc_stats: tuple, file_path: str) -> None:
    """
    Writes the document statistics as a JSON string to a file.

    
    See:
        stats_to_json

    Args:
        doc_stats (tuple | list): the document statistics
        file_path (str): The path of the file to be written.
    """
    ... # replace with your code, ... is same as pass


def stats_to_json(doc_stats: tuple) -> str:
    """
    Writes the document statistics as a JSON string, format would be:
    {"lines": 1, "words": 2, "vowels": 3, "palindromes": 4, "sentence_palindromes": 5}
    with the numbers replaced with the actual values.

    Examples:
        >>> stats_to_json((1, 2, 3, 4, 5))
        '{"lines": 1, "words": 2, "vowels": 3, "palindromes": 4, "sentence_palindromes": 5}'
        >>> stats_to_json((0, 0, 0, 0, 0))
        '{"lines": 0, "words": 0, "vowels": 0, "palindromes": 0, "sentence_palindromes": 0}'
        >>> stats_to_json((12, 102, 33, 42, 0))
        '{"lines": 12, "words": 102, "vowels": 33, "palindromes": 42, "sentence_palindromes": 0}'

    Args:
        doc_stats (tuple | list): the document statistics

    Returns:
        str: the JSON formatted string
    """
    return '' # replace with your code


if  __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
