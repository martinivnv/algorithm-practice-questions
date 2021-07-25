# Write code to remove duplicates from an unsorted linked list. 
# FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?
# 07 25 2021

# Hints:
# Have you tried a hash table? You should be able to do this in a single pass of the linked list
# Without extra space, you'll need O(N^2) time. Try using two pointers, where the second one searches ahead of the first one.

from singly_linked_list import Node, SLinkedList

class Solver(object):
    def __init__(self):
        pass

    def remove_dups(self, node):
        dataset = set(())
        previous = None
        while node != None:
            if node.data in dataset:
                previous.next = node.next
            else:
                dataset.add(node.data)
                previous = node
            node = node.next

if __name__ == "__main__":
    list = SLinkedList()
    list.head = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    e4 = Node("Thu")
    e5 = Node("Tue")
    e6 = Node("Fri")

    list.head.next = e2
    e2.next = e3
    e3.next = e4
    e4.next = e5
    e5.next = e6

    list.print_list()
    s = Solver()
    s.remove_dups(list.head)
    list.print_list()