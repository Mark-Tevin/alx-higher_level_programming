def uppercase(s):
    """
    Print a string in uppercase followed by a new line.

    Parameters:
    s (str): The string to print.

    Returns:
    None
    """
    uppercase_str = ""
    for c in s:
        if 'a' <= c <= 'z':
            # Convert lowercase character to uppercase using ASCII values
            uppercase_str += chr(ord(c) - 32)
        else:
            uppercase_str += c
    
    print(uppercase_str)  # Print the uppercase string
    print()  # Print a new line
