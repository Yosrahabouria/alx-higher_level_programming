#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
d = abs(number) % 10
if number < 0:
    d = -d
    if d > 5:
        print(f"Last digit of {number:d} is {d:d} and is greater than 5", end="")
    elif d == 0:
        print(f"Last digit of {number:d} is {d:d} and is 0", end="")
else:
    print(f"Last digit of {number:d} is {d:d} and is less than 6 and not 0")
