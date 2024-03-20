#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints the keys of a dictionary in sorted order.

    Args:
        a_dictionary (dict): The input dictionary.
    """
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
