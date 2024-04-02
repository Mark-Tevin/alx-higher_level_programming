#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for n in range(x):
            print("{:d}".format(my_list[n]), end='')
            count += 1
    except(TypeError, ValueError):
        pass
    print()
    return count
