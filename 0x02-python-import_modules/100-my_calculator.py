#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul
    if len(sys.argv) != 4:
        print(" Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit (1)
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        o = int(sys.argv[2])
        if o == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif o == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif o == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        elif o == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
