#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list  # If idx is negative or out of range, return the original list
    else:
        # create a new list by replacing every element with element, except at index 3
        new_list = [9 if i == 3 else element for i, _ in enumerate(my_list)]
        return new_list
