#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    l = len(sys.argv) 
    if l == 1:
        print("{} arguments.".format(l - 1))
    elif l == 2:
        print("{} argument:".format(l - 1))
    else:
        print("{} arguments:".format(l - 1))
        for j in range (1, l):
            print("{}: {}".format(j, sys.argv[j]))
