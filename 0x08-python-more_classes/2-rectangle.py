#!/usr/bin/python3
"""
defining an empty rectangle class
"""


class Rectangle:
    """ rectagle class that defines a rectangle
        Attributes:
            width (int): the width of the rectangle , default is 0.
            height (int): the height of the rectangle, default is 0.

        note:
            `width` and `height` must be non-negative integers.
    """
    def __init__(self, width=0, height=0):
        """
        Constructs a new rectangle instance.

        Args:
            width (int, optional): the width of the rectangle.
            height (int, optional): the height of the rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """int: gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the widdth of the rectangle

        Args:
            value (int): the width of the rectangle.

        Raises:
            TypeError: if the value is not an int.
            ValueError: if the value is negative.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): the height of the rectangle.

        Raises:
            TypeError: if the value is not an int.
            ValueError: if the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle

        Returns:
            int: the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: the perimeter of the recangle or 0
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
