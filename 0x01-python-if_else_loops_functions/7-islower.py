#!/usr/bin/python3

def islower(c):
    # Check if the ASCII value of the character is in the lowercase range
    return ord('a') <= ord(c) <= ord('z')

# Example usage
print(islower('a'))  # True
print(islower('A'))  # False
print(islower('1'))  # False
