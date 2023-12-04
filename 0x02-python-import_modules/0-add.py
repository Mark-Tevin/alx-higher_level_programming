#!/usr/bin/python3

from add_0 import add
a = 1
b = 2
output = add(a,b)
print("{} + {} = {}".format(a, b, output))

if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    
