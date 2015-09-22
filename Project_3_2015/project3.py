################################################################
#                                                              #
#                   CS 260 Programming Assignment 3            #
#                                                              #
#                   Written by Andrew Nelson                   #
#                                                              #
#                   February 2015                              #
#                                                              #
################################################################

import sys

class Node():           # Represents one Node of a Linked List data structure
    
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
class LinkedList():     # Represents a Linked List data structure
    
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        self.direction = True
        self.place = self.head      # Pointer to the current Node
        self.n = None               # max value a nodes data can be

    def createList(self, n):        # Creates a list the length of a given integer
        self.n = eval(n)
        for i in range(0,n+1,1):
            self.addNode(Node(i))
        self.place = self.head 

    def changeDirection(self):      # Changes the direction, affects the move, copy, and remove functions
        if self.direction:
            self.direction = False
        else:
            self.direction = True
    
    def increment(self):            # Increments the current Node by 1
        self.place.data = (self.place.data + 1) % self.n
    
    def decrement(self):            # Decrements the current Node by 1
        self.place.data = (self.place.data - 1) % self.n

    def copy(self):                 # Copies the current node and places it either before or after itself
        if self.direction:
            temp = self.place.prev
            self.place.prev = Node(self.place.data)
            temp.next = self.place.prev
            temp.next.prev = temp
            temp.next.next = self.place
            if self.place.prev.prev == self.tail:
                self.head = self.place.prev
            if self.place.prev.next == self.head:
                self.tail = self.place.prev


        else:
            temp = self.place.next
            self.place.next = Node(self.place.data)
            temp.prev = self.place.next
            temp.prev.next = temp
            temp.prev.prev = self.place
        
            if self.place.next.prev == self.tail:
                self.head = self.place.next
            if self.place.next.next == self.head:
                self.tail = self.place.next

   
    def move(self, n, m):           # Moves the current pointer a certain distance based on a given integer
        if self.direction:
            for i in range(0,n,1):
                self.place = self.place.next
        
        else:
            for i in range(0,m,1):
                self.place = self.place.prev
    
    def remove(self):               # Removes the current node and moves the current pointer to the next or previous node

#        print("REMOVE")
#        print("Place:", self.place.data)       # Used to debug
#        print("Prev:", self.place.prev.data)
#        print("Next:", self.place.next.data)

        if self.place.next == self.place and self.place.prev == self.place: 
            print(self.place.data)                                              # Ends the program
            
            self.place = None
            self.head = None
            self.tail = None

        else:
            temp = self.place
            if self.direction:
                self.place = temp.prev

            else:
                self.place = temp.next
            
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.prev = None
            temp.next = None

            if self.place.prev == self.tail:
                self.head = self.place
            if self.place.next == self.head:
                self.tail = self.place

    def addNode(self,node):                     # Adds a node onto the end of the array with the given data
        if self.head == None:
            self.head = node
            self.tail = node
            node.prev = None
            node.next = None
        
        else:
            here = self.head
            while here.next != None:
                here = here.next
            
            here.next = node
            node.prev = here
            self.tail = node
            self.head.prev = self.tail
    
    def read(self,ray):                         # Reads and performs the given input until the list is empty
        n = eval(ray[1]) 
        m = eval(ray[2])
        while self.place != None:
            for i in ray[3]:
                if self.place == None:
                    break
                if i == 'm':
                    self.move(n,m)
                if i == 't':
                    self.changeDirection()
                if i == 'i':
                    self.increment()
                if i == 'd':
                    self.decrement()
                if i == 'c':
                    self.copy()
                if i == 'r':
                    self.remove()

def main():
    inp = []
    for i in range(0,4,1):    
        inp.append(input())
     
    nums = LinkedList()

    nums.createList(eval(inp[0]))
    nums.read(inp)
main()    
