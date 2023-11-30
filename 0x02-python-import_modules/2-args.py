#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    l =len(sys.argv) - 1

    if l == 0:
        print("{} argument".format(l))
    elif l == 1:
        print("{} argument".forma(l))
    else:
        print("{}argumet".format(l))

    for j in range (l):
        print("{} : {}".format(j + 1, sys.argv[j + 1]))

