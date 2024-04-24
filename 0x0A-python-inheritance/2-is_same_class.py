#!/usr/bin/python3
"""Checks if the object is exactly an instance of the specified class."""


def is_same_class(obj, a_class):

    """Return true is object is an instance of the class,
    otherwise return False"""
    return type(obj) == a_class
