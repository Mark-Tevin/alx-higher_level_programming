#!/usr/bin/python3
"""This modeule contains a defination of a class
that inherits from int
"""


class MyInt(int):
    """Invert int operator == and !="""

    def __eq__(self, value):
        """== Overides != behaviour"""
        return self.real != value

    def __ne__(self, value):
        """Overide != operator with == behaviour"""
        return self.real == value
