#!/usr/bin/python3
"""This file inherits from the lists class"""


class MyList(list):
    def print_sorted(self):
        """Prints list in sorted order (ascending)."""
        # sort the list and print the list in acending order
        print(sorted(self))
