# Implement a binary tree from scratch
# Assume no duplicates allowed
# 07 29 2021

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    # In-order traversal
    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()

if __name__ == "__main__":
    tree = Node(8)
    tree.insert(4)
    tree.insert(10)
    tree.insert(2)
    tree.insert(6)
    tree.insert(20)
    tree.print()
