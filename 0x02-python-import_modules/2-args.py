#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1

plural = "arguments" if num_args > 1 else "argument"
print(f"Number of {plural}: {num_args}")

if num_args > 0:
    # Directly start listing arguments without a colon
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"\n{i}: {arg}", end="")
    # Print a final newline for formatting
    print()  # Add this line to ensure a newline at the end
