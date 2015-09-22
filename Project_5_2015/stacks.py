################################################################
#                                                              #
#                   CS 260 Programming Assignment 5            #
#                                                              #
#                   Written by Andrew Nelson                   #
#                                                              #
#                   March 2015                                 #
#                                                              #
################################################################

# This file is used to define the classes environmentNode, environmentList, environmentStack, expressionNode, and expressionStack

class environmentNode:
    def __init__(self,x,y,next=None):
        self.x = x                                                  # Node class with 2 data entries, one for the letter and one for the value
        self.y = y
        self.next = next

class environmentList:
    def __init__(self, head=None):
        self.head = head                                            # List for the stack representing each level of scope
        self.next = None
        self.len = 0

    def add(self,x,y):
        new = environmentNode(x,y)
        if self.head == None:
            self.head = new
        else:                                                        # Add a single node to the back of the list
            temp = self.head
            while temp!=None:
                temp=temp.next
            temp.next = new
        self.len+=1

class environmentStack:                                             # Stack holding each scope represented as a list that holds each variable for that scope
    def __init__(self,):
        self.top = environmentList()                                # Automatically made with a list, no need to make your own
    
    def push(self):
        li = environmentList()
        li.next = self.top
        self.top = li                                               # Pushes one node to a new scope that is placed on top of the stack

    def pop(self):
        temp = self.top
        self.top = temp.next                                        # Returns the most recent scope entered and removes it off the stack
        return temp                                                 # Returns the ENTIRE scope as an environmentList, not just a node!

class expressionNode:
    def __init__(self,x,next=None):                                 # Node with 1 data entry, for either a number or math expression 
        self.x = x
        self.next = next

class expressionStack:
    def __init__(self,top=None):                                    # Stack used to perform math within the program, and use order of operations
        self.top = top

    def push(self,x):
        node = expressionNode(x)                                  # Pushes a new node onto the stack, this needs to be a number or one of the following symbols: '+,-,*,/,^'
        node.next=self.top
        self.top = node
        
    def pop(self):
        temp = self.top                                             # Removes the last item pushed onto the stack and returns it
        self.top = temp.next
        return temp
