#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1  # Exclude the script name
    
    if num_args == 0:  # Handle the case of no arguments
        print("0")
    else:
        # Convert arguments to integers and sum them up
        sum_of_args = sum(int(arg) for arg in sys.argv[1:])
        print(sum_of_args)
