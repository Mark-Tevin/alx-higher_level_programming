#!/usr/bin/python3

# print numbers from 0 to 99 in the specified format
for num in range(100):
    print("{:02d}".format(num), end=", " if num < 99 else "\n")
