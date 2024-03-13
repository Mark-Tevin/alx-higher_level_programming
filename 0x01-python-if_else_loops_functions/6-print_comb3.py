#!/usr/bin/python3

# Print all possible combinations of two digits where 01 and 10 are considered the same combination
for i in range(10):
    for j in range(i+1, 10):
        print("{:d}{:d}".format(i, j), end=', ')
print()
