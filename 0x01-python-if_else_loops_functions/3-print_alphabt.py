#!/usr/bin/python3
# Program to print ASCII alphabet in lowercase (excluding 'q' and 'e') without a new line
print("".join("{}".format(chr(char)) for char in range(ord('a'), ord('z') + 1) if chr(char) not in ('q', 'e')), end='')
