class Node:
    def __init__(self, data, successor):
        self.data = data
        self.succ = successor


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        self.head = Node(data, self.head)
