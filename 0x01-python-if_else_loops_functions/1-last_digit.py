#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Extracting the last digit of the number
last_digit = abs(number) % 10

# Printing the message in the desired format
print("Last digit of", number, "is", last_digit, "and", end=" ")

# Checking conditions and printing the corresponding message
if last_digit > 5:
    print("is greater than 5")
elif last_digit == 0:
    print("is zero")
else:
    print("is less than 6 and not 0")

