#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    result = 0

    for num in my_list:
        if num not in new_list:
            result += num
            new_list.append(num)

    return result

