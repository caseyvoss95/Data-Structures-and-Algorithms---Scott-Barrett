class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        return
    
    def prepend(self, value):
        return
    
    def insert(self, index, value):
        return

linkedList = LinkedList(7)
print(linkedList.head.value)

# This file is a code-along to a course lecture
# I hand-typed each line of code, but it is NOT my own.

# ALL CREDITS TO:
# Data Structures & Algorithms - Python
# by Scott Barrett
# visit https://www.udemy.com/course/data-structures-algorithms-python/
# to purchase this fabulous course!