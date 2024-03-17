#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        if idx == 3:
            new_list = [9 if i == 3 else val for i, val in enumerate(my_list)]
            return new_list
        else:
            return my_list
