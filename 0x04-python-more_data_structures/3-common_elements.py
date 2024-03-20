def common_elements(set_1, set_2):
    """
    Finds common elements between two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: The set containing common elements.
    """
    if set_1 & set_2:  # Checks if there are common elements
        return set_1 & set_2  # Returns the common elements
    else:
        return set()  # Returns an empty set if there are no common elements
