#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
d = abs(number) % 10
if number < 0:
    d = -d
    print("Last digit of {} is {} and is ".format(number, d), end="")
if d > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, d), end="")
elif d == 0:
    print("Last digit of {} is 0".format(number), end="")
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, d), end="")
