#!/usr/bin/python3
"""Module for the add_integer function"""


def add_integer(a, b=98):
    """
    a function that adds two integers

    Args:
        a: the first integer
        b: the second integer

    Raises:
        TypeError: if one if the args isnt an int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
