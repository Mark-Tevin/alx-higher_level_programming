#!/usr/bin/python3
# Program to print ASCII alphabet in lowercase (excluding 'q' and 'e') without a new line
print(''.join(chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in ('q', 'e')), end='')

