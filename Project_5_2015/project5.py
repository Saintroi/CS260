################################################################
#                                                              #
#                   CS 260 Programming Assignment 5            #
#                                                              #
#                   Written by Andrew Nelson                   #
#                                                              #
#                   March 2015                                 #
#                                                              #
################################################################
from stacks import *
from scanner import Scanner
import sys

def read(ev, ex):
s = Scanner("")

while i = s.readChar():
    if i == '{':
        ev.push()
    
    else if i == '}':
        ev.pop()
    
    else if i == '@':
        c = s.readLine()
        for q in c:
            if q.isLower():
#            if q != ',' and q != ';':
                ev.top.add(q,0)
    
    else if i == '?':
        c = s.readLine()
        for q in c:
            if q.isLower():
#            if q!= ',' and q!= ';':
                while true:
                    f = ev.top.head
                    if f.x == q:
                        print(q + ' = ' + f.y)
                        break
                    else:
                        f = f.next
    else if i.isLower():
        c = s.readLine():
        c = c[1:len(c)-1]
        math(i,c)

                


def main():
evStack = environmentStack()
exStack = expressionStack()
read(esStack, exStack)

main()





