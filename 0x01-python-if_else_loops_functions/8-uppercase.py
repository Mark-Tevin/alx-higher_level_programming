#!/usr/bin/python3

def uppercase(t):
    output = ""
    for char in t:
        if 'a' <= char <= 'z':
            output += "{}".format(chr(ord(char) - 32))
        else:
            output += char
    print(output)
