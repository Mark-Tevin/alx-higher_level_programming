#!/usr/bin/python3
import sys

def add_args():
    num_argmnt = len(sys.argv)
    print(f"{num_argmnt - 1} argument{'s' if (num_argmnt - 1) != 1 else ''}:", end='')

    # Print ": " or "."
    if num_argmnt > 1:
        print(" ")

        R = sum(int(sys.argv[j]) for j in range(1, num_argmnt))
        print(R)
    else:
        print(".")
if __name__ == "__main__":
    add_args()

