################################################################
#                                                              #
#                   CS 260 Programming Assignment 2            #
#                                                              #
#                   Written by Andrew Nelson                   #
#                                                              #
#                   February 2015                              #
#                                                              #
################################################################

import sys

def read(filename):                 # Reads the file line by line and places it into a 2D array (Python list)
    f = open(filename)
    ray1 = []
    for line in f:
        line.strip()
        ray1.append(line.strip().split(','))
    return ray1

def notRead(ray, filename):         # Writes the sorted array to the given file
    f = open(filename, 'w')
    for i in ray:
        for c in i:
            if c != i[len(i)-1]:
                f.write(str(c) + ',')
            else:
                f.write(str(c))
        f.write('\n')    

def cwidFix(ray):
    for i in ray:
        if i[3] == 0:
            i[3] = '00000000'
    return

def helper(ray, colNum, var,descending ):       # Does the actual sorting
    if var == 'int':
        for i in range(1,len(ray),1):
           ray[i][colNum] = int(ray[i][colNum])

    if var == 'string':
        for i in range(1,len(ray),1):
            ray[i][colNum] = str(ray[i][colNum])

    if var == 'float':
        for i in range(1,len(ray),1):
            ray[i][colNum] = float(ray[i][colNum])
        
    unsortedRay = ray[1:]
    if descending:
        sortedRay = sorted(unsortedRay, key=lambda x:x[colNum], reverse = True)
    else:
        sortedRay = sorted(unsortedRay, key=lambda x:x[colNum])
    sortedRay.insert(0, ray[0])
    return sortedRay
 
def sort(ray, filename):             # Sorts the array according to the second input file
    f = open(filename)
    methodRay = []
    for line in f:
        methodRay.append(line.strip().split(','))
    for i in range (len(methodRay)-1,-1,-1):           # Uses helper to sort backwards
        colNum = ray[0].index(methodRay[i][0])
        if methodRay[i][1] == 'ascend':
            ray = helper(ray,colNum,methodRay[i][2],False)
        else:
            ray = helper(ray,colNum,methodRay[i][2],True)
    cwidFix(ray)    
    return ray

           

def main():
    ray = read(sys.argv[1])
    ray = sort(ray,sys.argv[2])
    notRead(ray, sys.argv[3])

main()    
    
