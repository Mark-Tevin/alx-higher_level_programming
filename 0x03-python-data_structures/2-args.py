#!/usr/bin/python3
def print_arg(argv):
    arg = len(argv) - 1
    if arg == 0:
        print("{:d} argument.".format(arg))
        return
    else:
        if arg == 1:
            print("{:d} argument:".format(arg))
        else:
            print("{:d} arguments:".format(arg))
        j = 1
        while j <= arg:
            print("{:d}: {:s}".format(j, argv[j]))
            j += 1

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
