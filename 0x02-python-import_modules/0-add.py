#!/usr/bin/python3
from add_0 import add

a = 1
b = 2

def addition():
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result), end=' ')

if __name__ == '__main__':
    addition()  # Call the function to print the result
