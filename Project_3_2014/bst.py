# ****BST CLASS****
# ****Written by Andrew Nelson, November 2014****
# ****For CS260 Programming Assignment 3****
# ****This class serves as a Binary Search Tree****

from bstnode import *

class BST:
    
    def __init__(self, level):
        self.root = None
        self.size = 0
        self.level = level
    
    def __len__(self):
        return self.size

    def __contains__(self, target):
        
        def recurse(node):
            return node != None and (node.data == target or (target < node.data and recurse(node.left)) or 
 recurse(node.right))            
        return recurse(self.root)

    def isEmpty(self):
        return self.size == 0

    def add(self, item):
        
        def recurse(node):
            if item < node.data:
                if node.left is None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            elif node.right is None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
        if self.isEmpty():
            self.root = BSTNode(item)
        else:
            recurse(self.root)
        self.size += 1

    def preOrder(self):

        def recurse(node):
            if node!=None:
                lyst = list()
                lyst.append(node.data)
                if node.left:
                    lyst.append(recurse(node.left))
                if node.right:
                    lyst.append(recurse(node.right))
                return lyst

        return recurse(self.root)

    def postOrder(self):

        def recurse(node):
            if node!=None:
                lyst = list()
                if node.left:
                    lyst.append(recurse(node.left))
                if node.right:
                    lyst.append(recurse(node.right))
                lyst.append(node.data)
                return lyst

        return recurse(self.root)
    
    def inOrder(self):

        def recurse(node):
            if node!=None:
                lyst = list()
                if node.left:
                    lyst.append(recurse(node.left))
                lyst.append(node.data)
                if node.right:
                    lyst.append(recurse(node.right))
                return lyst
        return recurse(self.root)

    def levelOrder(self):
        level = self.level
        lyst = []
        q = False
        for i in level:
            if i > level[0]:
                q = False
                break
            else:
                q = True
        if q:
            for i in level:
                lyst.append([i])
        z = False
        for i in level:
            if i < level[0]:
                z = False
                break
            else:
                z = True
        if z:
            for i in level:
                lyst.append([i])
        
        if not q and not z:
            lyst.append([level[0]])
            del level[0]
            k = 1
            while len(level)>0:
                lost = []
                for i in range(0,2**k,1):
                    try:
                        lost.append(level[0])
                        del level[0]
                    except IndexError:
                        break
                k+=1        
                lyst.append(lost)
        return lyst     
