#!/usr/bin/python3
"""Module defines a linked list node class"""


class Node:
    """docstring for Node."""
    def __init__(self, data: int, next_node=None):
        self.data = data
        self.next_node = next_node
        return

    @property
    def data(self):
        """The data property getter."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The data property getter."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for data

        Args:
            value (Node): Pointer to next node
        """
        if type(value) == Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")
        return
    pass


class SinglyLinkedList:
    """docstring for SinglyLinkedList"""
    def __init__(self):
        """Constructor for SinglyLinkedList"""
        self.__head: Node | None = None
        pass

    def sorted_insert(self, value):
        """Inserts a new node at the correct sorted position

        Args:
            value (int): data of a singly linked list
        """
        if self.__head is None:
            self.__head = Node(value)
        else:
            tr = self.__head
            if tr.data > value:
                self.__head = Node(value, tr)
            while tr.next_node is not None:
                if tr.next_node.data >= value and tr.data <= value:
                    tr.next_node = Node(value, tr.next_node)
                    break
                else:
                    tr = tr.next_node
            if tr.next_node is None and tr.data < value:
                tr.next_node = Node(value)

    def __str__(self):
        """Return a printable representation of created object"""
        string: str = ""
        t = self.__head
        while t is not None:
            string += str(t.data)
            if t.next_node is not None:
                string += '\n'
            t = t.next_node
        return string
