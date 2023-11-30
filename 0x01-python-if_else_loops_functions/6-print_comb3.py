#!/usr/bin/python3

# Prints all possible different combinations of two digits
for tens_dig in range(10):
    for units_digit in range(tens_dig + 1, 10):
        print("{:d}{:d}".format(tens_dig, units_digit), end=", " if units_digit < 9 else "\n")
