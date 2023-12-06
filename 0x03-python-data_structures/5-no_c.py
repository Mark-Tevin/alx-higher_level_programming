#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all occurrences of 'c' and 'C' from a string.

    Parameters:
        - my_string (str): Input string.
    """
    new_char = ''
    for char in my_string:
        if char.lower() != 'c':
            new_char += char
    return new_char
