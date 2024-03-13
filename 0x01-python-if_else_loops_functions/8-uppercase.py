#!/usr/bin/python3

def uppercase(s):
    """
    Print a string in uppercase followed by a newline.

    Parameters:
    s (str): The string to convert to uppercase and print.
    """
    # Initialize an empty string to store the uppercase version
    upper_string = ""

    # Iterate over each character in the string
    for char in s:
        # Convert the character to uppercase using ASCII values
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - 32)  # Convert lowercase to uppercase
        else:
            upper_char = char  # Keep non-alphabetic characters unchanged
        # Append the uppercase character to the result string
        upper_string += upper_char

    # Print the uppercase string followed by a newline
    print(upper_string, end='\n')
