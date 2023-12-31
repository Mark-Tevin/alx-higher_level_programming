#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints integers in reverse order in a list.

    Param:
        - my_list (list): List of integers.
    """
    if isinstance(my_list, list):
        my_list.reverse()
        for j in my_list:
            print("{:d}".format(j))
