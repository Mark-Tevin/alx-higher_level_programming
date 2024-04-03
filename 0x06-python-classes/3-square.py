#!/usr/bin/python3

"""Define class square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """instantiation.
        Parameters:
            size: size of the newly created square
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of square"""
        return (self.__size * self.__size)
