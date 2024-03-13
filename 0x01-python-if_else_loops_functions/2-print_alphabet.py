#!/usr/bin/python3
#Print ASCII alphabet in lowercase using a single print statement with string format
print(''.join(chr(i) for i in range(97, 123)).format(), end='')
