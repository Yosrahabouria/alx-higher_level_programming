#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb = 0

    for a in range(0, x):
        try:
            print("{}".format(my_list[a]), end="")
            nb += 1
        except IndexError:
            continue
        print("")
        return nb
