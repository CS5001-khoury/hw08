"""
Homework 08: Document Statistics
===========================
Course:   CS 5001

PROVIDED CODE - no need to edit! 

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

