#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Adds or updates a key-value pair in the dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key: The key to add or update.
        value: The value associated with the key.

    Returns:
        dict: The updated dictionary.
    """
    new_dict = a_dictionary.copy()  # Create a copy of the original dictionary
    new_dict[key] = value  # Add or update the key-value pair in the new dictionary
    return new_dict  # Return the updated dictionary
