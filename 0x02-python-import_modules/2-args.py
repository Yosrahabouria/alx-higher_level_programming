#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    l = len(sys.argv) - 1
    if l == 0:
        print("0 arguments.")
    elif l == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(1))
    for j in range(l):
        print("{}: {}".format(j + 1, sys.argv[j + 1]))
