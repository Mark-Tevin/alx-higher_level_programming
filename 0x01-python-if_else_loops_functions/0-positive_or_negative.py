#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# print a randomn number

if number > 0: #positive and negative check
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
