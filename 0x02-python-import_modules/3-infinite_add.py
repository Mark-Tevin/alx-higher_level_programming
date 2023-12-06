#!/usr/bin/python3

def sum_all(*args):
    sum = 0

    for num in args:
        if not str(num).replace('-', '').isdigit():
            return False
        else:
            sum += int(num)
    return sum

if __name__ == "__main__":
    import sys
    result = sum_all(*sys.argv[1:])
    print(result)
