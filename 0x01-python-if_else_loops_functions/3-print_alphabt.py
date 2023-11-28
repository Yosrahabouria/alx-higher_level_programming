#!/usr/bin/python3
"""prints the ASCII alphabet, in lowercase, not followed by a new line"""
for l in range(97, 123):
    if chr(l) != 'q' and chr(l) != 'e':
        print("{}".format(chr(l)), end="")
