#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position without modifying the original list.

    Parameters:
        - my_list (list): List of elements.
        - idx (int): Index where the element should be replaced.
        - element: New element to be placed at the specified index.

    Returns:
        - List: A new list with the replacement if successful, otherwise, returns a copy of the original.
    """
    if 0 <= idx < len(my_list):
        # Create a new list with original elements and the replacement
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
    else:
        # Return a copy list if idx is negative or out of range
        return my_list
