from __future__ import annotations


class Node:
    def __init__(self, data, successor: Node):
        self.data = data
        self.succ = successor

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.string = "None"

    def add(self, data) -> None:
        """
        Add element to the front of the list
        """
        self.head = Node(data, self.head)

    def __str__(self) -> str:
        string = ""
        current = self.head
        while current is not None:
            string += str(current.data) + " -> "
            current = current.succ
        string += "None"
        return string

    @staticmethod
    def reverse_linked_list(lst: LinkedList) -> LinkedList:
        """
        Returns a new list with reversed list elements of input list.

        This method assumes the linked list input is acyclic.
        """
        reversed_list = LinkedList()
        if lst.head is None:
            # handle empty list case
            return reversed_list
        current = lst.head
        # traverse the list until the next node is None (end of list)
        while current is not None:
            reversed_list.add(current.data)
            current = current.succ
        return reversed_list
