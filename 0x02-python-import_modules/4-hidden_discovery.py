#!/usr/bin/python3

import uncompyle6  # Library for decompiling .pyc files
import re

if __name__ == "__main__":
    # Decompile the .pyc file
    with open("hidden_4.pyc", "rb") as f:
        source = uncompyle6.decompile_file(f.read())

    # Extract names using a regular expression
    names = re.findall(r"def ([a-zA-Z_]\w*)\(", source)

    # Filter out names starting with _ and sort alphabetically
    filtered_names = [name for name in names if not name.startswith("_")]
    filtered_names.sort()

    # Print names, one per line
    for name in filtered_names:
        print(name)
