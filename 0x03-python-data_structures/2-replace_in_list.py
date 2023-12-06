#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces elements at a specific position.

    Params:
        - my_list (list): List of elements.
        - idx (int): Index where the element should be replaced.
        - element: New element to be placed at the specified index.

    Returns:
        - List: The modified list if the replacement is successful, otherwise, returns the original list.
    """
    if (idx < 0) or (idx > len(my_list) - 1):
        return my_list
    else:
        my_list[idx] = element
        return my_list
