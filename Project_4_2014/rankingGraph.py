#### Written by Andrew Nelson, December 2014 ####
#### This program serves as a football team ranking system ####
#### Using Weighted Directed Graphs ####
#### Written for CS260 Project number 4 ####
import sys

class teamNameNode():
    def __init__(self, name,rank = None, nex =None):
        self._name = name
        self._next = nex
        self._rank = rank
        self._win = 0
        self._loss = 0
        self._tie = 0

    def getName(self):
        return self._name

    def next(self):
        return self._next
    
    def getRank(self):
        return self._rank
    
    def setRank(self, rank):
        self._rank = rank
class gameNode():
    def __init__(self, score, name, left, right=None):   
                                                 # A positive score will imply the team in the first node won
        self._score = score                      # A negative number will imply the team in this node won
        self._name = name                        # Score is difference between the 2
        self._left = left
        self._right = right                      # Left is previous, Right is next
    
    def getScore(self):
        return self._score
    
    def getName(self):
        return self._name

    def right(self):
        return self._right
    
    def left(self):
        return self._left

class teamRankingGraph():
    def __init__(self, filename, year = None):
        self._ray = []
        self._year = year
        self._file = filename
        self.read(filename)
    
    def getYear(self):
        return self._year
    
    def getGraph(self):
        return self._ray

    def addTeam(self, name, nex = None):
        node = teamNameNode(name)
        self._ray.append(node)
        if nex:
            node._next = nex 

    def addGame(self, prev, name, score, nex= None):
        for i in self._ray:
            if i.getName() == prev:
                if score > 0:
                    i._win += 1
                elif score < 0:
                    i._loss += 1
                else:
                    i._tie += 1
                if not i.next():
                    i._next = gameNode(score, name, i)
                else:
                    node = i.next()
                    while node.right():
                        node = node.right()
                    node._right = gameNode(score, name, node)
    def rank(self):
            for i in self.getGraph():
                node = i.next()
                add = 0
                c = 0
                while node:
                    add += node.getScore()
                    node = node.right()
                    c+=1

                i.setRank(add / c)
            originalRank = {}
            newRank = {}
            for i in self.getGraph():
                #print(i.getRank())
                originalRank[i.getName()] = i.getRank()
                newRank[i.getName()] = i.getRank()
            a = 0
            for i in range(0, 5000, 1):
                a +=1
                #print(a)
                schedFact = {}
                for j in self.getGraph():
                    schedFact[j.getName()] = 0
                    c = 0
                    node = j.next()
                    while node:
                        schedFact[j.getName()] += newRank[node.getName()] 
                        c+=1
                        node = node.right()
                        
                    if c > 0:
                        schedFact[j.getName()] = schedFact[j.getName()] / c
                j.setRank(schedFact[j.getName()] + originalRank[j.getName()])
                newRank[j.getName()] = (schedFact[j.getName()] + originalRank[j.getName()])
    
    def order(self):
        for i in range(1, len(self.getGraph()),1):
            for j in range(1, len(self.getGraph()),1):
                if self.getGraph()[j-1].getRank() < self.getGraph()[j].getRank():
                    temp = self.getGraph()[j-1]
                    self.getGraph()[j-1] = self.getGraph()[j]
                    self.getGraph()[j] = temp
    def display(self):
        self.order()
        name = "output_1"+self._file
        out = open(name,'w')
        
        out.write("Rank Team                            W-L-T    Rating\n")
        c =1 
        for i in self._ray:
            out.write("  "+str(c)+"  "+i.getName() + ' '*(32- int(len(i.getName()))))
            out.write(str(i._win) + '-' + str(i._loss) + '-' + str(i._tie)+'    ')
            out.write(str(round(i.getRank(),3))+ '\n') 
            c+=1

    def read(self, filename):
        f = open(filename)
        ray = []
        team = []
        ray = f.readlines()
        for l in ray:
            team1 = l[:32].strip()
            team2 = l[36:68].strip()
            score1 = eval(l[33:36])
            score2 = eval(l[68:])
            if team1 not in team:
                self.addTeam(team1)
                team.append(team1)

            if team2 not in team:
                self.addTeam(team2)
                team.append(team2)
            self.addGame(team1, team2, score1 - score2)
            self.addGame(team2, team1, score2 - score1)
        f.close()

def main():
    one = teamRankingGraph(sys.argv[1])
    one.rank()
    one.display()
main()    

