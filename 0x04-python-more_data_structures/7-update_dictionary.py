#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Adds or updates a key-value pair in a dictionary.

    Args:
        a_dictionary (dict): The original dictionary.
        key: The key to add or update.
        value: The value corresponding to the key.

    Returns:
        dict: The updated dictionary.
    """
    new_dict = a_dictionary.copy()  # Create a copy of the original dictionary
    if key in new_dict:
        # If the key exists in the dictionary, replace its value
        new_dict[key] = value
    else:
        # If the key doesn't exist, create a new key-value pair
        new_dict[key] = value
    return new_dict
