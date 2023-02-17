#!/usr/bin/python3
"""Module defines Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor method for Square method

        Args:
            self (Square): Referring to current class
            size (int): Size of Square
        """
        self.size = size
        self.position = position
        return

    @property
    def size(self):
        """The size property getter."""
        return self.__size

    @size.setter
    def size(self, sz: int):
        """Set the size property

        Args:
            size (int): Size of square
        """
        if type(sz) != int:
            raise TypeError("size must be an integer")
        if sz < 0:
            raise ValueError("size must be >= 0")
        self.__size = sz
        return

    @property
    def position(self):
        """The position property getter."""
        return self.__position

    @position.setter
    def position(self, pos):
        """Set the position property

        Args:
            size (int): Size of square
        """
        if type(pos) == tuple and len(pos) == 2 and type(pos[0]) == int and \
           type(pos[1]) == int and pos[0] >= 0 and pos[1] >= 0:
            self.__position = pos
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Print square to terminal"""
        if self.size:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
        else:
            print()
    pass
