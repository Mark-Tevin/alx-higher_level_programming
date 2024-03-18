#!/usr/bin/python3

# Using tranlate method to remove both 'c' and 'C' from a string
def no_c(my_string):
    new_string = my_string.translate({ord('c'): None, ord('C'): None})
    return new_string
