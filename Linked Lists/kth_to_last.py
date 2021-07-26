# Implement an algorithm to find the kth to last element of a singly linked list.
# 07 26 2021

# Hints:
# What if you knew the linked list size? What is the difference between finding the Kth-tolast element and finding the Xth element? 
# If you don't know the linked list size, can you compute it? How does this impact the runtime?
# Try implementing it recursively. If you could find the (K-l)th to last element, can you find the Kth element?
# You might find it useful to return multiple values

from singly_linked_list import Node, SLinkedList 

class Solver(object):
    def __init__(self):
        pass

    # O(N) time complexity and O(1) space complexity
    def find(self, linked_list, k):
        last = linked_list.head
        for i in range(k-1):
            last = last.next
            if last is None:
                return "Node not found"
        kth_to_last = linked_list.head
        while last.next is not None:
            kth_to_last = kth_to_last.next
            last = last.next
        return kth_to_last.data

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

    s = Solver()
    print(s.find(list, 2))
    print(s.find(list, 3))
    print(s.find(list, 4))
    print(s.find(list, 5))
    print(s.find(list, 6))