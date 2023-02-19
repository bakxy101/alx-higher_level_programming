#!/usr/bin/python3
"""Module defines adder function"""


def add_integer(a, b=98):
    """Returns integer sum of a and b

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        integer sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
