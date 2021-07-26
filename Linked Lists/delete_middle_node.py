# Implement an algorithm to delete a node in the middle (i.e., any node but 
# the first and last node, not necessarily the exact middle) of a singly linked
# list, given only access to that node.
# 07 26 2021

from singly_linked_list import Node, SLinkedList

class Solver(object):
    def __init__(self):
        pass

    # O(1) time complexity
    def delete(self, list, node):
        if node is None or node.next is None:
            return False
        next_node = node.next
        node.data = next_node.data  # Copy the data from the next node to the given node
        node.next = next_node.next  # Delete the next node
        return True

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