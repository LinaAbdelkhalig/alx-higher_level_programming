#!/usr/bin/python3
"""Module for print_square function"""


def print_square(size):
    """
    prints a square with the # character

    Args:
        size: the size of square

    Raises:
        TypeError: if size is not an int
        ValueError: if the size is less than 0
        TypeError: if size is float and is less than 0

    Return:
        the printed square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
