#!/usr/bin/python3
"""Checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """
    Return True if the object is an instance of the specified class.

    Args:
        obj: Any object.
        a_class: Class to compare against.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return True if type(obj) is a_class else False
