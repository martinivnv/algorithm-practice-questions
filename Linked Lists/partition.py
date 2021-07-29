# Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only 
# need to be after the elements less than x (see below). The partition element x can appear anywhere 
# in the "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
# 07 26 2021

# Hints:
# Consider that the elements don't have to stay in the same relative order. We only need
# to ensure that elements less than the pivot must be before elements greater than the pivot.

from singly_linked_list import Node, SLinkedList

class Solver:
    def __init__(self):
        pass

    # O(N) time complexity and O(1) space complexity
    def partition(self, list, x):
        node = list.head
        prev = None
        pivot_node = None
        # Find the pivot node and make it the list head
        while node is not None:
            if node.data == x:
                pivot_node = node
                if pivot_node != list.head:
                    prev.next = pivot_node.next
                    pivot_node.next = list.head
                    list.head = pivot_node
                break
            else:
                prev = node
                node = node.next
        # If x is not in list, make the head node the pivot node
        if pivot_node is None:
            pivot_node = list.head

        prev = pivot_node
        node = pivot_node.next
        next_node = None
        while node is not None:
            if node.data >= x:
                next_node = node.next
                prev = node
            elif node.data < x:
                # Remove from its current position
                next_node = node.next
                prev.next = node.next
                # Add node to front of list
                node.next = list.head
                list.head = node
            node = next_node

if __name__ == "__main__":
    list = SLinkedList()
    list.head = Node(3)
    e2 = Node(5)
    e3 = Node(8)
    e4 = Node(5)
    e5 = Node(10)
    e6 = Node(2)
    e7 = Node(1)

    list.head.next = e2
    e2.next = e3
    e3.next = e4
    e4.next = e5
    e5.next = e6
    e6.next = e7

    s = Solver()
    list.print_list()
    s.partition(list, 5)
    list.print_list()