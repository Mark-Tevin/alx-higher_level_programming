#!/usr/bin/python3
def no_of_argu(argv):
    num_arg = len(argv) - 1
    if num_arg == 0:
        print("{:d} argument.".format(num_arg))
        return
    else:
        if num_arg == 1:
            print("{:d} argument:".format(num_arg))
        else:
            print("{:d} arguments.".format(num_arg))
        n = 1
        while n <= num_arg:
            print("{:d}: {:s}".format(n, argv[n]))
            n += 1

if __name__ =="__main__":
    import sys
    no_of_argu(sys.argv)
