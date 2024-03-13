def islower(c):
    """
    Check if a character is lowercase.

    Parameters:
    c (str): The character to check.

    Returns:
    bool: True if the character is lowercase, False otherwise.
    """
    # Check if the ASCII value of the character falls within the range of lowercase letters
    return ord('a') <= ord(c) <= ord('z')
