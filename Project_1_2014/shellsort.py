def readGaps(gaps):
    read = open(gaps)
    gap = []
    i = 0
    for line in read:
        gap.append(eval(line))
        i+=1
    return gap 

def readInput(inp):
    given = int(input("How many lines need to be sorted? "))
    read = open(inp)
    sThis=[]
    for i in range (0,given,1):
        sThis.append(eval(read.readline()))
        i+=1
    return sThis

def out(sThis):
    O=open("output.txt","w")
    for i in sThis:
        O.write(str(i))
        O.write("\n")

def shellSort(gap, sThis):
    swap = 0
    comp = 0
    for g in gap:
        while g >0:
            for i in range(g, len(sThis)):
                val = sThis[i]
                j=i
                while j >= g and sThis[j-g] > val:
                    comp +=2
                    sThis[j] = sThis[j-g]
                    swap+=1
                    j -= g
                sThis[j] = val
                swap+=1
            g //=2
    print(swap,"swaps")
    print(comp,"comparisons")
    out(sThis)
    return sThis

def main():
    shellSort(readGaps("gaps.txt"), readInput("input.txt"))

main()
