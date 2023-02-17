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
        self.size = size
        return

    @property
    def size(self):
        """Getter of size property

        Returns:
            size private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size property

        Args:
            size (int): Size of square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)
    pass
