#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializes the newly created rectangle.

        Args:
            width (int): width of rectangle
            height (int): height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value
