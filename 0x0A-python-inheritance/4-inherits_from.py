#!/usr/bin/python3
"""This module checks if  is an instance of a class
that inherited (directly or indirectly)
from the specified class.
"""


def inherits_from(obj, a_class):
    """Function checks if object is an instance of a class
    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if is an instance of subclass,
    else False if otherwise.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
