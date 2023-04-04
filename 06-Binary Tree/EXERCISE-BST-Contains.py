class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            elif temp.value > value:
                if temp.left:
                    temp = temp.left
                else:
                    return False
            else:
                if temp.right:
                    temp = temp.right
                else:
                    return False
        

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.contains(27))

print('\nBST Contains 17:')
print(my_tree.contains(17))

print("\nTesting all other nodes")
print(my_tree.contains(82))
print(my_tree.contains(52))
print(my_tree.contains(18))
print(my_tree.contains(76))
print(my_tree.contains(21))
print(my_tree.contains(47))

print("\nTesting bogus nodes")
print(my_tree.contains(822))
print(my_tree.contains(19))
print(my_tree.contains(5))
print(my_tree.contains(-99))
print(my_tree.contains(42))
print(my_tree.contains(46))

"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""