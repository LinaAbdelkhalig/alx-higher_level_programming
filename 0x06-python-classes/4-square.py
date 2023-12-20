#!/usr/bin/python3
"""actual square module"""


class Square:
    """this class defines a square"""

    def __init__(self, size=0):
        """constructor

        Args:
            size: the size of the square
        """
        self.size = size

    @property
    def size(self):
        """retriever

        Returns:
            the size attr
        """
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the area of the square

        Returns:
            the area
        """
        return self.__size * self.__size
