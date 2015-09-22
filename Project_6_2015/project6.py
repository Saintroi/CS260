################################################################
#                                                              #
#                   CS 260 Programming Assignment 4            #
#                                                              #
#                   Written by Andrew Nelson                   #
#                                                              #
#                   March 2015                                 #
#                                                              #
################################################################

import sys

class Node:                                   # Building Block for both the Queue and Stack classes                  
    def __init__ (self, x, y, n = None):        # NOTE: This node has 2 data entries rather than the usual one. I didn't know how else to emplement it without a python list.
        self.x = x
        self.y = y
        self.next = n

class Heap:                                # Class representation of a Heap 
    def __init__(self, comp):
        self.isMin = comp
        self.array = list()
        self.n = 0
    
    def __repr__(self):
        return self.array.__repr__()

    def size(self):
        return self.n

    def isEmpty(self):
        return self.n == 0

    def add(self, x, y):
        p = Node (x,y)
        self.array.append(p)
        pos = len(self.array)-1
        self.n += 1

        while pos > 0:
            parent = (pos -1) // 2
            pitem = self.array[parent].y
            if (pitem <= y and self.isMin) or (pitem >= y and not self.isMin):
                break
            else:
                self.array[pos] = self.array[parent]
                self.array[parent] = p
                pos = parent

    def remove(self):                    # Returns the NODE NOT the data inside it as it would normally do.
        if self.isEmpty():
            raise KeyError ("Queue is empty.")
        self.n -= 1
        top = self.array[0]
        bot = self.array.pop(len(self.array)-1)
        if len(self.array) == 0:
            return bot
        
        self.array[0] = bot
        last = len(self.array)-1
        pos = 0
        while True:
            
            left = 2 * pos + 1
            right = 2 * pos + 2
            if (left > last) :
                break
            if right > last:
                maxC = left
            else:
                leftI = self.array[left]
                rightI = self.array[right]
                if (leftI.y < rightI.y and self.isMin) or (leftI.y > rightI.y and not self.isMin):
                    maxC = left
                else:
                    maxC = right
            maxI = self.array[maxC]
            if (bot.y <= maxI.y and self.isMin) or (bot.y >= maxI.y and not self.isMin):
                break
            else:
                self.array[pos] = self.array[maxC]
                self.array[maxC] = bot
                pos = maxC
        return top

    def __iter__(self):
        temp = list(self.array)
        result = []
        while not self.isEmpty():
            result.append(self.remove())
        self.array = temp
        self.n = len(self.array)
        return iter(result)
    

class BSTNode:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.left = None
        self.right = None

class BST:                                        # A Binary Search Tree to hold the heaps
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None

    def insert (self, x, y):                     # Where X is the Stock Name and Y is the Heap    
        def recurse (p):
            if x<p.x:
                if p.left==None:
                    p.left = BSTNode (x,y)
                else:
                    recurse (p.left)
            else:
                if p.right==None:
                    p.right = BSTNode (x,y)
                else:
                    recurse (p.right)
        
        if self.root==None:
            self.root = BSTNode(x,y)
        else:
            recurse (self.root)

    def find(self,x):
        def recurse(p):
            if p == None:
                return BSTNode(False,p)
            elif x < p.x:
                return recurse(p.left)
            elif x > p.x:
                return recurse(p.right)
            else:
                return BSTNode(True, p)

        return recurse(self.root)        

def remove (self, x):
        if not self.find(x):
            raise KeyError("Item does not exist.")
        
        def recurse (p):
            # Modify this method.
            parent = p
            cur = p.left
            while not cur.right == None:
                parent = cur
                cur = cur.right
            p.x = cur.x
            if parent == p:
                p.left = cur.left
            else:
                parent.right = cur.left
        
        if self.root == None:
            return None
        item = None
        pre = Node(None)
        pre.left = self.root
        parent = pre
        direc = 'L'
        cur = self.root
        while not cur == None:
            if cur.x == x:
                item = cur.x
                brea =ecur
            if cur.x > x:
                direc = 'L'
                cur = cur.left
            else:
                direc = 'R'
                cur = cur.right

        if item == None: return None

        if not cur.left == None and not cur.right == None:
            recurse(cur)
        else:
        
            if cur.left == None:
                new = cur.right

            else:
                new = cur.left

            if direc == 'L':
                parent.left = new
            
            else:
                parent.right = new

        if self.root != None:
            self.root = pre.left

        return item    



def fifo(filename, namefile):                   # Calculates stock gains and losses using the "first in first out" method.
    f = open(filename)
    w = open(namefile, 'w') 
    fifo = Queue()
    transaction = 0
    for line in f:
        ln = line.split()
        if ln[0] == "Buy":
            fifo.enqueue(eval(ln[1]), eval(ln[2]))
        else:
             
            if fifo.size() == 0:
                raise KeyError("No stocks to sell")
            
            shares = eval(ln[1])
            cost = eval(ln[2])
            total = shares * cost

            while True:
                if fifo.front.shares > shares:
                    total = total - (shares * fifo.front.cost)
                    fifo.front.shares = fifo.front.shares - shares
                    break
                elif fifo.front.shares == shares:
                    total = total - (shares * fifo.front.cost)
                    fifo.dequeue()
                    break
            
                else:
                    total = total - (fifo.front.shares * fifo.front.cost)
                    shares = shares - fifo.front.shares
                    fifo.dequeue()

            if total > 0:
                w.write("Gain = "+"{:.2f}".format(total)+ '\n')

            elif total == 0:
                w.write("Zero"+ '\n')

            else:
                w.write("Loss = "+"{:.2f}".format(total)+'\n')

            transaction += total
    w.write("Total = "+"{:.2f}".format(transaction))
    f.close()
    w.close()

def maxH():
    bst = BST()
    f = open(sys.argv[1])
    w = open(sys.argv[3], 'w')
    transaction = 0
    for line in f:
        ln = line.split()
        if bst.find(ln[2]).x:
            xam = bst.find(ln[2]).y.y
        else:
            bst.insert(ln[2], Heap(False))
            xam = bst.find(ln[2]).y.y
        
        if ln[0] == "Buy":
            xam.add(eval(ln[1]),eval(ln[3]))
        
        else:

            if xam.isEmpty():
                bst.remove(ln[2])
                raise KeyError("No stocks to sell")
            
            shares = eval(ln[1])
            cost = eval(ln[3])
            total = shares * cost

            while True:
                front = xam.remove()
                if front.x > shares:
                    total = total - (shares * front.y)
                    front.x = front.x - shares
                    xam.add(front.x,front.y)
                    break
                
                elif front.x == shares:
                    total = total - (shares*front.y)
                    break

                else:
                    total = total - (front.x * front.y)
                    shares = shares - front.x
            if total > 0:
                w.write("Gain = "+"{:.2f}".format(total)+ '\n')

            elif total == 0:
                w.write("Zero"+ '\n')

            else:
                w.write("Loss = "+"{:.2f}".format(total)+'\n')

            transaction += total

    w.write("Total = "+"{:.2f}".format(transaction))
    f.close()
    w.close()

def minH():
    bst = BST()
    f = open(sys.argv[1])
    w = open(sys.argv[2], 'w')
    transaction = 0
    for line in f:
        ln = line.split()
        if bst.find(ln[2]).x:
            xam = bst.find(ln[2]).y.y
        else:
            bst.insert(ln[2], Heap(True))
            xam = bst.find(ln[2]).y.y
        
        if ln[0] == "Buy":
            xam.add(eval(ln[1]),eval(ln[3]))
        
        else:

            if xam.isEmpty():
                bst.remove(ln[2])
                raise KeyError("No stocks to sell")
            
            shares = eval(ln[1])
            cost = eval(ln[3])
            total = shares * cost

            while True:
                front = xam.remove()
                if front.x > shares:
                    total = total - (shares * front.y)
                    front.x = front.x - shares
                    xam.add(front.x,front.y)
                    break
                
                elif front.x == shares:
                    total = total - (shares*front.y)
                    break

                else:
                    total = total - (front.x * front.y)
                    shares = shares - front.x
            if total > 0:
                w.write("Gain = "+"{:.2f}".format(total)+ '\n')

            elif total == 0:
                w.write("Zero"+ '\n')

            else:
                w.write("Loss = "+"{:.2f}".format(total)+'\n')

            transaction += total

    w.write("Total = "+"{:.2f}".format(transaction))
    f.close()
    w.close()


def main():                                 # Drives the program
    maxH()
    minH()
main()
