#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        msg = "arguments."
    elif len(argv) > 2:
        msg = "arguments:"
    else:
        msg = "argument:"

    print("{:d} {:s}".format(len(argv) - 1, msg))

    for idx, arg in enumerate(argv[1:]):
        print("{:d}: {:s}".format(idx + 1, arg))
