#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
d = abs(number) % 10
if number < 0:
    d = -d
    print(f"Last digit of {number:d} is {d:d} and is ", end=" ")
if d > 5:
    print("greater than 5", end=" ")
elif:
    print("0", end=" ")
else:
    print("less than 6 and not 0")