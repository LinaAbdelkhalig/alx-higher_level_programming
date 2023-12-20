#!/usr/bin/python3
"""actual square module"""


class Square:
    """this class defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """constructor

        Args:
            size: the size of the square
            position: the position of the square
        """
        self.size = size
        self.__position = position

    @property
    def position(self):
        """retriever

        Returns:
            the private instance property position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter

        Args:
            value: the value of the position
        """
        if isinstance(value, tuple):
            for i in value:
                if not isinstance(i, int) or i < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    def my_print(self):
        """ prints the square with #

        Returns:
            nothing
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print("_", end="")
                for i in range(self.__size):
                    print("#", end="")
                print("")
