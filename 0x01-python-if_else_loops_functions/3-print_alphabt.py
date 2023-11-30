#!/usr/bin/python3
# Print ASCII alphabet in lowercase excluding 'q' and 'e' without a new line
for char in range(ord('a'), ord('z') + 1):
    if chr(char) not in ['q', 'e']:
        print("{}".format(chr(char)), end="")
