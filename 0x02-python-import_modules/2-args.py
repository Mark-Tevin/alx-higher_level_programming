#!/usr/bin/python3
import sys

def print_arg():
    arg = sys.argv[1:]
    num_args = len(arg)

    print(f"Number of argument{'s' if num_args != 1 else ''}: {num_args}", end='')

    #print ": " or "."
    if num_args > 0:
        print(":", end='\n')
    else:
        print(".", end='\n')
        return

    #print each argument with its position
    for i,arg in enumerate(arg, start = 1):
        print(f"{i}: {arg}")
if __name__ == "__main__":
    print_arg()
