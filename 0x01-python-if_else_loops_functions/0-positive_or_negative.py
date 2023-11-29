#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# print a randomn number
print(f"The number is: {number}")

if number > 0: #positive and negative check
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
