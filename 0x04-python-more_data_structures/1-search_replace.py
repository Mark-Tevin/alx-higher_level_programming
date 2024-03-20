#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Searches for a specific element in a list and replaces it with a new element,
    returning a new list with the replacements.

    Args:
        my_list (list): The input list.
        search: The element to search for.
        replace: The element to replace with.

    Returns:
        new_list: The new list with replacements.
    """
    return [replace if item == search else item for item in my_list]
