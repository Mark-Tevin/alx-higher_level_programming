#!/usr/bin/python3

# Program to print all possible different combinations of two digits
for tens in range(9):
    for ones in range(tens + 1, 10):
        print("{:d}{:d}".format(tens, ones), end=", " if ones < 9 else "\n")
