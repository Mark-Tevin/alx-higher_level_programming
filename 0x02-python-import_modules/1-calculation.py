#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

#variables
a = 10
b = 5

# Call function and print the result
reslt_add = add(a, b)
reslt_sub = sub(a, b)
reslt_mul = mul(a, b)
reslt_div = div(a, b)

# Display the results (4 print statements)
print(f"Addition: {reslt_add}")
print(f"Subtraction: {reslt_sub}")
print(f"Multiplication: {reslt_mul}")
print(f"Division: {reslt_div}")

