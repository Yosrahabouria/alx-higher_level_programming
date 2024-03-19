#!/usr/bin/python3
import hidden_4 as hidden
import sys
if __name__ != "__main__":
    exit()

    for j in dir(hidden):
        if j[:2] != "__":
            print(j)
