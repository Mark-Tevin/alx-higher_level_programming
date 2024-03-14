#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    # Check if the number of arguments is not 3
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Extracting arguments
    a = float(sys.argv[1])
    operator = sys.argv[2]
    b = float(sys.argv[3])

    # Validating operator
    if operator not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Perform the operation
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    else:
        result = div(a, b)

    # Print the result
    print("{} {} {} = {}".format(a, operator, b, result))
