################################################################
#                                                              #
#                   CS 260 Programming Assignment 1            #
#                                                              #
#                   Written by Andrew Nelson                   #
#                                                              #
#                   January 2015                               #
#                                                              #
################################################################
import sys

def min(li):
    temp = li[0]
    for i in li:
        if i < temp:
            temp = i
    return temp

def max(li):    
    temp = li[0]
    for i in li:
        if i > temp:
            temp = i
    return temp

def sum(li):
    temp = 0
    for i in li:
        temp += i
    return temp

def getInput(inFile = None):
    if inFile:
        f = open(inFile)
        putIn = f.read().split()
        putIn = list(map(int, putIn))
        f.close()
    else:
        putIn=''
        while True:
            try:
                tup = input()
                if tup != '' and tup != '\n':
                    putIn += ' ' + (tup)
            except EOFError:
                break
        putIn = putIn.split()
        putIn = list(map(int, putIn))
    return putIn

def noneInput(putIn, outFile = None):
    if outFile:
        o = open(outFile,'w')
        o.write("number = 0\n")
        o.write("minimum = none\n")
        o.write("maximum = none\n")
        o.write("sum = 0\n")
        o.write("product = 1\n")
        o.write("average = none\n")
        o.write("median = none\n")
        o.write("modes = []\n")
        o.close()
    else:
        print("number = 0")
        print("minimum = none")
        print("maximum = none")
        print("sum = 0")
        print("product = 1")
        print("average = none")
        print("median = none")
        print("modes = []")

def product(li):
    temp = 1
    for i in li:
        temp = temp*i
    return temp    

def getOutput(putIn,outFile = None):
    if len(putIn) < 1:
        noneInput(putIn, outFile)
        return 
    if outFile:
        o = open(outFile,'w')
        o.write("number = "+ str(len(putIn))+'\n')
        o.write("minimum = "+ str(min(putIn))+'\n')
        o.write("maximum = "+ str(max(putIn))+'\n')
        o.write("sum = "+ str(sum(putIn))+'\n')
        o.write("product = "+ str(product(putIn))+'\n')
        o.write("average = "+ str(sum(putIn) / float(len(putIn)))+'\n')
        srted = sorted(putIn)
        if not((len(srted)/2).is_integer()):
            med = srted[int(len(srted)/2)]
        else:
            med = (srted[int((len(srted)/2))] + srted[int((len(srted)/2))-1])/2    
        o.write("median = "+ str(med)+'\n')    
        mo = {}
        mode = [] 
        for i in putIn:
            try:
                mo[i] += 1
            except KeyError:    
                mo[i] = 1
        xam = max(list(mo.values()))
        for i in mo.keys():
            if mo[i] == xam:
                mode.append(i)

        o.write("modes = "+ str(sorted(mode))+'\n')
        o.close()
    else:
        print("number =", len(putIn))
        print("minimum =", min(putIn))
        print("maximum =", max(putIn))
        print("sum =", sum(putIn))
        print("product =", product(putIn))
        print("average =", sum(putIn) / float(len(putIn)))
        srted = sorted(putIn)
        if not((len(srted)/2).is_integer()):
            med = srted[int(len(srted)/2)]
        else:
            med = (srted[int((len(srted)/2))] + srted[int((len(srted)/2))-1])/2    
        print("median =", med)    
        mo = {}
        mode = [] 
        for i in putIn:
            try:
                mo[i] += 1
            except KeyError:    
                mo[i] = 1
        xam = max(list(mo.values()))
        for i in mo.keys():
            if mo[i] == xam:
                mode.append(i)

        print("modes =", sorted(mode))

def main():
    if len(sys.argv) > 2:
        getOutput(getInput(sys.argv[1]), sys.argv[2])
    
    elif len(sys.argv) > 1:
        getOutput(getInput(sys.argv[1]))

    else:
        getOutput(getInput())
main()    

