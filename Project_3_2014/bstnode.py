# ****BST NODE CLASS****
# ****Written by Andrew Nelson, November 2014****
# ****For CS260 Programming Assignment 3****
# ****This class serves as a base for a Binary Search Tree****

class BSTNode:
    def __init__(self, item, left=None, right=None):
        self.data = item
        self.left = left
        self.right = right
    
    def hasLeft(self):
        return self.left != None
    
    def hasRight(self):
        return self.right != None
    
    
