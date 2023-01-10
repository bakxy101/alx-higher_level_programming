#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    op_list = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
            }
    b = 5
    a = 10
    for sign, op in op_list.items():
        print("{:d} {:s} {:d} = {:d}".format(a, sign, b, op(a, b)))
