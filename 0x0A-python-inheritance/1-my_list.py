#!/usr/bin/python3
"""This module inherits from the list class"""


class MyList(list):
    def print_sorted(self):
        """Prints the list in sorted order (ascending)."""
        print(sorted(self))
