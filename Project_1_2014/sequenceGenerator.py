def Hibbard(big):
    H = open("Hibbard.txt","w")
    i = 1
    math = (2**i)-1
    while math <= big:
        H.write(str(math))
        H.write("\n")
        i+=1
        math = (2**i)-1

def Pratt(big):
    P = open("Pratt.txt","w")
    Pr = []
    q = 0
    while 3**q <= big:
        p = 0 
        while (2**p)*(3**q) <= big:
            Pr.append((2**p)*(3**q))
            p+=1
        q+=1
    Pr.sort()
    for i in Pr:
        P.write(str(i))
        P.write("\n")
def SedA(big):
    SA = open("SedgewickA.txt","w")
    SA.write("1\n")
    i = 1 
    math = (4**i)+3*2**(i-1)+1
    while math <= big:
        SA.write(str(math))
        SA.write("\n")
        i+=1
        math = (4**i)+3*2**(i-1)+1

def SedB(big):
    SB = open("SedgewickB.txt","w")
    B = []
    i = 1 
    math = (9*(4**(i-1)-2**(i-1))+1)
    while math <= big:
        B.append(math)
        i+=1
        math =(9*(4**(i-1)-2**(i-1))+1)
    
    k=1
    math_b = (4**(k+1)-6*(2**k)+1)
    while math_b <= big:
        B.append(math_b)
        k+=1
        math_b = (4**(k+1)-6*(2**k)+1)
        
    B.sort()
    for p in B:
        SB.write(str(p))
        SB.write("\n")

def main():
    big = int(input("Enter the largest gap: "))
    Hibbard(big)
    Pratt(big)
    SedA(big)
    SedB(big)

main()
