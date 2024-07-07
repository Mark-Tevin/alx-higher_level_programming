#!/usr/bin/python3
"""Finds a peak in alist of integers"""


def find_peak(list_of_integers):
    """ Function that finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): a list of integers

    This algorithm oughts to have the lowest complexity.
    NB: there is more than one peak in a list

    The most naive solution is to just go thru each elemet
    one after the other to see if it's a qualified peak. This solution will
    definetly take O(n) time complexity at the worst case and O(1) for space
    complexity which is super for most algorithm problem.
    The tricky part is to solve it with O(log(n)) time complexity

    Usually Binary Search is being used in sorted arrays(also known as 
    Bitonic array, or a sorted array), this case is different as we can't
    sort the array.

    In Binary Search, we always check the middle value and see if its
    qualified to be the peak, else we change the start or end pointer
    so as to get a new middle value.

    Returns:
        int: peak(s)
    """
    arr = list_of_integers
    # if there is no list of int return None
    if arr == []:
        return None
    length = len(arr)

    start, end = 0, length -1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid + 1]:
            return arr[mid]
        if arr[mid - 1] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return arr[start]
