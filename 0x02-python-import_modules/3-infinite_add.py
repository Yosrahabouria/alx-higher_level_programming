#!/usr/bin/python3
if __name__ == "__main__":
    """print infinite adds of arguments"""
    import sys
    s = 0
    l = len(sys.argv)
    for i in range(1, l):
        s += int(sys.argv[i])
        print("{}".format(s))
