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
        else:
            temp = self.root
            while temp:
                if temp.value == value:
                    return False
                elif temp.value < value:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right = new_node
                        return True
                else:
                    if temp.left:
                        temp = temp.left
                    else:
                        temp.left = new_node
                        return True



my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
my_tree.insert(7)
my_tree.insert(-33)


"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""


print('Root:', my_tree.root.value)            
print('Root->Left:', my_tree.root.left.value)        
print('Root->Right:', my_tree.root.right.value)        
print('Root->Right-Right:', my_tree.root.right.right.value)        
print('Root->Left-Left:', my_tree.root.left.left.value)        



"""
    EXPECTED OUTPUT:
    ----------------
    Root: 2
    Root->Left: 1
    Root->Right: 3

"""