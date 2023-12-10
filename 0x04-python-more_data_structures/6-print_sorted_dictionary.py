#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Parameters:
    - a_dictionary (dict): The input dictionary.

    Returns:
    - None
    """
    if a_dictionary:
        for key in (a_dictionary):
            print("{}: {}".format(key, a_dictionary[key]))
