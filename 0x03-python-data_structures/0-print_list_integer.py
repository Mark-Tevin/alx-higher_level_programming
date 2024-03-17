#!/usr/bin/python3
'''
function that prints all integers of a list.

'''
def print_list_integer(my_list=[]):
    """
    prints out all the elements listed in the list called my_list

    Argv:
    my_list (list): The list to be printed and defauls to an empty list
    """
    for item in my_list:
        print("{}".format(item))
