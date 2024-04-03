#!/usr/bin/python3

"""Define class square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """instantiation.
        Parameters:
            size: size of the newly created square
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """Get position of square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if(not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns current area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with # """
        if self.__size == 0:
            print("")
            return

        [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(self.__position[0])]
            [print("#", end="") for i in range(self.__size)]
            print("")
