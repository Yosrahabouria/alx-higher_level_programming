#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """find peak definition"""
    l = 0
    r = len(list_of_integers) - 1

    while l < r:
        mi = (l + r) // 2
        if list_of_integers[mi] < list_of_integers[mi + 1]:
            l = mi + 1
        else:
            r = mi

    return list_of_integers[l]
