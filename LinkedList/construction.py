class Node:
    def __init__(self,value):
        self.value = value
        self.tail = None
        self.head = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, node):
        if (node == self.head):
            self.head = self.head.next
        if (node == self.tail):
            self.tail = self.tail.prev
        self.removeWithBindings(node)
    
    def removeWithBindings(node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

