#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb = 0
    for a in range(0, x):
        try:
            print("nb_print: {:d}".format(my_list[a]), end="")
            nb += 1
        except:
            continue
        print("")
        return (nb)
