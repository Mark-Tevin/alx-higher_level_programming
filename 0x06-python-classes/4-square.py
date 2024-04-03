#!/usr/bin/python3

"""Define class square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """instantiation.
        Parameters:
            size: size of the newly created square
        """
        self.__size = size

    @property
    def size(self):
        """sets size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current area"""
        return (self.__size * self.__size)
