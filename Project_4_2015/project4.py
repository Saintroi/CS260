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
        self.shares = x
        self.cost = y
        self.next = n

class Queue:                                # Class representation of a Queue
    def __init__(self):
        self.front = None
        self.back = None
        self.n = 0

    def size(self):
        return self.n

    def isEmpty(self):
        return self.n == 0

    def enqueue(self, x, y):
        p = Node (x,y)
        if self.isEmpty():
            self.front = p
        else:
            self.back.next = p
        self.back = p
        self.n += 1

    def dequeue(self):                          # Returns the NODE NOT the data inside it as it would normally do.
        if self.isEmpty():
            raise KeyError ("Queue is empty.")
        x = self.front
        self.front = self.front.next
        if self.front == None:
            self.back = None
        self.n -= 1
        return x

class Stack:                                    # Class representation of a Stack
    def __init__(self):
        self.top = None
        self.n = 0
    
    def size(self):
        return self.n

    def isEmpty(self):
        return self.top == None

    def push(self, x, y):
        self.top = Node(x, y, self.top)
        self.n += 1

    def pop(self):                              # Returns the NODE NOT the data inside it as it would normally do.
        if self.isEmpty():                                                      
            raise KeyError("Stack is empty.")
        x = self.top
        self.top = self.top.next
        self.n -= 1 
        return x


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

def lifo(filename,namefile):                        # Calculates stock gains and losses using the "last in first out" method.
    f = open(filename)
    w = open(namefile, 'w') 
    lifo = Stack()
    transaction = 0
    for line in f:
        ln = line.split()
        if ln[0] == "Buy":
            lifo.push(eval(ln[1]), eval(ln[2]))
        else:
             
            if lifo.size() == 0:
                raise KeyError("No stocks to sell")
            
            shares = eval(ln[1])
            cost = eval(ln[2])
            total = shares * cost

            while True:
                if lifo.top.shares > shares:
                    total = total - (shares * lifo.top.cost)
                    lifo.top.shares = lifo.top.shares - shares
                    break
                
                elif lifo.top.shares == shares:
                    total = total - (shares * lifo.top.cost)
                    lifo.pop()
                    break
            
                else:
                    total = total - (lifo.top.shares * lifo.top.cost)
                    shares = shares - lifo.top.shares
                    lifo.pop()

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

def average(filename, namefile):                # Calculates stock gaines and losses using a method of calculating the weighted average between each transaction
    f = open(filename)
    w = open(namefile, 'w')
    shares = 0
    prices = []
    transaction = 0
    for line in f:
        ln = line.split()
        if ln[0] == "Buy":
            shares += eval(ln[1])
            prices.append(eval(ln[2])* eval(ln[1]))
        else:
            total = eval(ln[1]) * eval(ln[2])
            avgpr = float(0)
            for price in prices:
                avgpr += price 
            avgpr = avgpr/shares    
            
            total = total - (avgpr * eval(ln[1]))
            if total > 0:
                w.write("Gain = "+"{:.2f}".format(total)+ '\n')

            elif total == 0:
                w.write("Zero"+ '\n')

            else:
                w.write("Loss = "+"{:.2f}".format(total)+'\n')
            
            shares -= eval(ln[1])
            transaction += total

            del prices[:]
            prices.append(avgpr * shares)    

    w.write("Total = "+"{:.2f}".format(transaction))
    f.close()
    w.close()

def main():                                 # Drives the program
    fifo(sys.argv[1], sys.argv[2])
    lifo(sys.argv[1], sys.argv[3])
    average(sys.argv[1], sys.argv[4])

main()
