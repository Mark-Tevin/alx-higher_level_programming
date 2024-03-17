#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list #if the idx is a negative or out of range retun the original list
    new_list = []
    for i, elem in enumerate(my_list):
        if i == 3:
            new_list.append(9)
        else:
            new_list.append(elem)
