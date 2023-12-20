#!/usr/bin/python3
"""actual square module"""


class Square:
    """this class defines a square"""

    def __init__(self, size=0):
        """constructor

        Args:
            size: the size of the square
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
