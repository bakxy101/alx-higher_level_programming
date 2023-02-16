#!/usr/bin/python3
"""Module defines Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Constructor method for Square method

        Args:
            self (Square): Referring to current class
            size (int): Size of Square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        return
    pass
