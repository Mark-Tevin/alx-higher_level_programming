#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer) and returns the result.

    Args:
        my_list (list): The input list.

    Returns:
        int: The sum of unique integers in the list.
    """
    unique_values = list(set(my_list))  # Extract unique values from the list
    result = sum(unique_values)  # Sum up the unique values
    return result
