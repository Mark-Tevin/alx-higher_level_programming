#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list  # If idx is negative or out of range, return the original list
    
    new_list = [9 if i == 3 else elem for i, elem in enumerate(my_list)]  # Enumerate and replace element at idx 3 with 9
    return new_list
