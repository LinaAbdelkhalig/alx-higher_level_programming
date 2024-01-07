#!/usr/bin/python3
"""Module for the say_my_name function"""


def say_my_name(first_name, last_name=""):
    """
    print My name is <first name> <last name>

    Args:
        first_name: the first name
        last_name: the last name

    Raises:
        TypeError: if either of the args is not a string

    Return:
        the printed text
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
