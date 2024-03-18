#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_result = []
    for x in my_list:
        if x > 0 and x % 2 == 0:
            list_result.append(x)
    return list_result
