#!/usr/bin/python3
"""prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase"""
a = 0
for b in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(b - a)) 
