#!/usr/bin/python3
"""
defining an empty rectangle class
"""


class Rectangle:
    """ rectagle class that defines a rectangle
        Attributes:
            width (int): the width of the rectangle , default is 0.
            height (int): the height of the rectangle, default is 0.
            number_of_instances (int): the number of instances made

        note:
            `width` and `height` must be non-negative integers.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructs a new rectangle instance.

        Args:
            width (int, optional): the width of the rectangle.
            height (int, optional): the height of the rectangle
        """
        Rectangle.number_of_instances += 1
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

    def __str__(self):
        """
        returns a user-friendly represeentation of the class

        Returns:
            str: thestring representation of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join(str(self.print_symbol) * self.width for _ in range(self.height))

    def __repr__(self):
        """
        Returns a dev friendly rep of the rectangle

        Returns:
            str: the string representatino of the rectangle
        """
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        """
        Prints a goodbye message when the instance is deleted>
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns which rectangle is bigger

        Args:
            rect_1: the 1st rectangle
            rect_2: the second rectangle

        Returns:
            Rectangle: the bigger rectangle

        Raises:
            TypeError: if one of the aargs is not a rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
