# Implement a stack from scratch
# 07 28 2021

class Stack(object):
    class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    def push(self, data):
        node = self.Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        node = self.top
        if self.top != None:
            self.top = self.top.next
        return node
    
    def peek(self):
        return self.top
    
    def is_empty(self):
        return self.top == None

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    top = stack.peek()
    print(top.data)             # 3
    print(stack.pop().data)     # 3
    print(stack.pop().data)     # 2
    print(stack.is_empty())     # False
    stack.pop()
    print(stack.is_empty())     # True