#!/usr/bin/python3

def uppercase(t):
    case = ""
    for char in t:
        if 'a' <= char <= 'z':
            case += "{}".format(chr(ord(char) - 32))
        else:
            case += char
    print(case)
