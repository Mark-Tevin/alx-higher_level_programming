#!/usr/bin/python3

# Print numbers from 0 to 99 in ascending order separated by ", " and ending with a newline
print(', '.join('{}' for _ in range(100)).format(*range(100)))
