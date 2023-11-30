#!/usr/bin/python3
# Program to print ASCII alphabet in lowercase without a new line
for char in range(ord('a'), ord('z') + 1):
    print("{}".format(chr(char)), end="")
print()
