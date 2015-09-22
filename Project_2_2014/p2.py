# Written by Andrew Nelson, October 2014
from List import *        

def multiply(one, two):
    lim = 0
    mult = {}

    for k in one.keys():
        if int(k) > lim:
            lim = int(k)

    for i in range(0,lim,1):
        row = []
        for j in range(0,lim,1):
            row.append(int(one[i][1+j]))            # Key Error, No time to debug, turning project in.
        col = []
        for j in two:
            for c in range(0,lim,1):
                if int(j[c]) == i:
                    col.append(int((j[c+1])))
                    break
        
        if i not in mult.keys():
            mult[i] = []
        for c in range(0,lim,1):
            ans = []
            while len(ans) < lim:
                for q in range(0, lim, 1):
                    ans.append(int(q))
                    ans[c] += row[q]*col[q]
                    

            multi[i].join(ans) 

def out(mult):
    lim = 0
    for k in mult.keys():
        if int(k) > lim:
            lim = int(k)

    for i in range(0,lim,1):
        count = 0
        print(i, end = '')
        for j in mult[i]:
            print(j,end='')
            count += 1
            if count == 1:
                print("\n")
                count = 0

def main():
    m1 = []
    line = input("Please enter your matrix values one line at a time, type \"0 0 0\" to stop: ") 
    while line != '0 0 0':
        if len(line) != 5:
            print("Syntax error, please restart the program and try again")
            exit()
        m1.append(line)
        line = input("Please enter the next line: ")
    
    sparse_one = {} 
    for i in m1:
        if i[0] in sparse_one.keys():
            sparse_one[i[0]].append(i[2])
            sparse_one[i[0]].append(i[4])
        else:
            sparse_one[i[0]] = [i[2],i[4]]
    m2 = [] 
    line = input("Please enter the information for your second matrix, type \"0 0 0\" to stop: ")
    while line!= '0 0 0':
        if len(line) != 5:
            print("Syntax error, please restart the program and try again")
            exit()
        m2.append(line)
        line = input("Please enter the next line: ")
    
    sparse_two = {} 
    for i in m2:
        if i[0] in sparse_two.keys():
            sparse_two[i[0]].append(i[2])
            sparse_two[i[0]].append(i[4])
        else:
            sparse_two[i[0]] = [i[2],i[4]]
    
    print(sparse_one)
    print(sparse_two)
    out(multiply(sparse_one, sparse_two))

main()        
