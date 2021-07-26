# Implement an algorithm to delete a node in the middle (i.e., any node but 
# the first and last node, not necessarily the exact middle) of a singly linked
# list, given only access to that node.
# 07 26 2021

from singly_linked_list import Node, SLinkedList

class Solver(object):
    def __init__(self):
        pass

    def delete(self, list, node):
        previous = None
        current = list.head
        while current.next is not None:
            if current.next == node:
                previous = current
                current = current.next
                previous.next = current.next
            else:
                current = current.next

if __name__ == "__main__":
    list = SLinkedList()
    list.head = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    e4 = Node("Thu")
    e5 = Node("Fri")

    list.head.next = e2
    e2.next = e3
    e3.next = e4
    e4.next = e5

    list.print_list()
    s = Solver()
    s.delete(list, e3)
    s.delete(list, Node("Sun"))
    list.print_list()