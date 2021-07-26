# You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. 
# Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912. 
# 07 26 2021

from singly_linked_list import Node, SLinkedList

class Solver(object):
    def __init__(self):
        pass

    # O(N) time complexity, N being the length of the longer list
    def get_sum(self, list1, list2):
        num1 = self.to_num(list1)
        num2 = self.to_num(list2)
        sum = num1 + num2
        list_final = SLinkedList()
        return self.to_list(list_final, sum)

    def to_num(self, list):
        node = list.head
        power = 0
        num = 0
        while node is not None:
            num += node.data * 10 ** power
            power += 1
            node = node.next
        return num

    def to_list(self, list, num):
        if num == 0:
            return list
        else:
            digit = num - num // 10 * 10 # Returns the number in the 1's column
            list.append_end(digit)
            return self.to_list(list, num // 10)
            


if __name__ == "__main__":
    s = Solver()

    list1 = SLinkedList()
    list2 = SLinkedList()

    list1 = s.to_list(list1, 617)
    list2 = s.to_list(list2, 295)
    
    sum = s.get_sum(list1, list2)
    sum.print_list()
