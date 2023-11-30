def uppercase(t):
    for char in t:
        if 'a' <= char <= 'z':
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print(char, end="")
    print()
