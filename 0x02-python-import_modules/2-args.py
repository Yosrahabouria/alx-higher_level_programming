#!/usr/bin/python3
if __name__ == "__main__":
    """prints the number of and the list of its arguments"""
    import sys

    l = len(sys.argv) - 1
    if l == 0:
        print(f"{l:d} arguments.")
    elif l == 1:
        print(f"{l:d} argument:")
    else:
        print(f"{l:d} arguments:")
    for j in range(l):
        print("{}: {}".format(j + 1, sys.argv[j + 1]))
