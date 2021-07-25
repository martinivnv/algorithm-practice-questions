# Implement a singly linked list from scratch
# 07 24 2021

class Node(object):
    def __init__(self, d):
        self.data = d
        self.next = None
    
class SLinkedList(object):
    def __init__(self):
        self.head = None
    
    # Adds node to start of list
    def append_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Adds node to end of list
    def append_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = new_node

    # Inserts new node after the given node
    def insert(self, given_node, data):
        if given_node is None:
            return "Node not found"
        else:
            new_node = Node(data)
            new_node.next = given_node.next
            given_node.next = new_node
    
    # Deletes a node by its key
    def remove(self, key):
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == key:
                prev = current_node
                current_node = current_node.next
                prev.next = current_node.next
                return "Node removed"
            current_node = current_node.next
        return "Key not found"
            
                    

    # Prints out the list values
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


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

list.append_beg("Sun")
list.append_end("Sat")

list.insert(e2, "Martinday")
list.print_list()
print(list.remove("Martinday"))
print(list.remove("Jubeday"))
list.print_list()