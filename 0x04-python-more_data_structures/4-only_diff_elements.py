#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Finds elements present in only one set.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: The set containing elements present in only one set.
    """
    od_set = set()  # Initialize the result set
    if set_1 ^ set_2:  # Checks if there are different elements between sets
        return set_1 ^ set_2
    else:
        return od_set #returns an empty set if there is no different element
