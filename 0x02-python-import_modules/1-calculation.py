#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

def addition():
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result), end='\n')
def minus():
    result = sub(a, b)
    print("{} - {} = {}".format(a, b, result), end='\n')
def times():
    result = mul(a, b)
    print("{} * {} = {}".format(a, b, result), end='\n')
def division():
    result = div(a, b)
    print("{} / {} = {}".format(a, b, result), end='\n')
    
if __name__ == '__main__':
    addition()
    minus()
    times()
    division()
