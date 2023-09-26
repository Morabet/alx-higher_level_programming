#!/usr/bin/python3
"""a module that implements a singly linked list"""


class Node:
    """a class that defines a node in a linked list"""

    def __init__(self, data, next_node=None):
        """Initialization a Node
        Args:
            data: the data in each node
            next_node: will holde the next node of class Node
        Raises:
            TypeError: data must be an integer.
            TypeError: next_node must be None or hold a Node object.
        """

        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        if not isinstance(next_node, self.__class__) and next_node:
            raise TypeError("next_node must be a Node object")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """a getter for the attribute data"""

        return self.__data

    @data.setter
    def data(self, value):
        self.__init__(value, self.__next_node)

    @property
    def next_node(self):
        """a getter for the attribute next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        self.__init__(self.__data, value)


class SinglyLinkedList:
    """Initialize the Singly Linked List class"""

    def __init__(self):
        """Insert a new Node to the SinglyLinkedList.
            The node is inserted into the list at the correct
            ordered numerical position.
        """
        self.__head = None

    def sorted_insert(self, value):
        """inset node to the linked list in a sorted manner"""

        if not self.__head:
            self.__head = Node(value)

        else:
            tmp = Node(value)
            current = self.__head

            if current.data > value:
                tmp.next_node = self.__head
                self.__head = tmp

            else:
                while current.next_node and current.next_node.data < value:
                    current = current.next_node

                tmp.next_node = current.next_node
                current.next_node = tmp

    def __str__(self):
        """override the __str__ for print to work"""

        current = self.__head
        string = []

        if current:
            while current:
                string.append(str(current.data))

                current = current.next_node

        return ("\n".join(string))
