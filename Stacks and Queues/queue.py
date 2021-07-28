# Implement a queue from scratch
# 07 28 2021

class Queue(object):
    class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        node = self.Node(data)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node

    def remove(self):
        if self.head is not None:
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return data
        else:
            return None

    def peek(self):
        return self.head

    def is_empty(self):
        return self.head is None

if __name__ == "__main__":
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    print(q.peek().data)    # 1
    q.remove()
    print(q.remove())       # 2
    print(q.remove())       # 3
    print(q.is_empty())     # False
    print(q.remove())       # 4
    print(q.is_empty())     # True




