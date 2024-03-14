#!/usr/bin/python3

def magic_calculation(a, b):
   """Performs a calculation based on the imported functions 'add' and 'sub'."""

   from magic_calculation_102 import add, sub  # Import required functions

   if a < b:
       c = add(a, b)  # Call 'add' if a is less than b
       for i in range(4, 6):
           c = add(c, i)  # Add 4 and 5 to the result
       return c  # Return the final value
   else:
       return sub(a, b)  # Call 'sub' if a is not less than b
