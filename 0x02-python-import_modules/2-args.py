import sys

num_args = len(sys.argv) - 1

plural = "arguments" if num_args > 1 else "argument"
print(f"Number of {plural}: {num_args}")

if num_args > 0:
    print(":", end="")  # Print a colon only if there are arguments
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"\n{i}: {arg}", end="")
