import sys
import os
import random

FILE_NAME = "config/"

class Peg:
    def __init__(self, pegId, items):
        self.items = items
        self.id = pegId

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None

        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def disksOn(self):
        return { self.id : [ aDisk.weight for aDisk in self.items]}
        # return "bla"
    
    def isEqual(self, aPeg, byId = False):
        if aPeg == None:
            return False
        if byId:
            return self.id == aPeg.id

        length = self.size()
        if length != aPeg.size():
            return False

        for i in range(length):
                for disk1, disk2 in zip(self.items, aPeg.items):
                    if disk1.weight != disk2.weight:
                        return False
        return True

    def isValid(self):
        length = len(self.items) - 1

        if length == 0:
            return True
        if len(self.items) % 2 != 0:
            return self.items[length].weight < self.items[length - 1].weight

        for i in range(length):
            twoDisks = self.items[i : i+2]
            print twoDisks[0].weight
            print twoDisks[1].weight
            if twoDisks[0].weight < twoDisks[1].weight:
                print 
                return False

        return True

class Disk:
    def __init__(self, weight):
        self.weight = weight

class State:
    def __init__(self, pegs):
        self.pegs = pegs

    def printState(self):
        # print "STATE"
        for peg in self.pegs:
            print peg.disksOn()

    def isEqual(self, aState):
        if len(self.pegs) != len(aState.pegs):
            return False
        else:
            length = len(self.pegs)
            for i in range(length):
                if not self.pegs[i].isEqual(aState.pegs[i]):
                    return False
            return True

    def isValid(self):
        for peg in self.pegs:
            if not peg.isValid():
                return False
        return True
    def randomValidPeg(self):
        length = len(self.pegs)
        randomIndex = random.randint(0, length-1)
        # print randomIndex
        randomPeg = self.pegs[randomIndex]
        # print randomPeg.disksOn()

        return randomPeg

        # print "\nfirst random peg is"
        # print randomPeg.disksOn()
        # print "source"
        # print source
        
        # if source == None or source.isEmpty():
        #     while randomPeg.isEmpty() and randomPeg.isValid() == False:
        #         randomIndex = random.randint(0, length-1)
        #         randomPeg = self.pegs[randomIndex]
        #         print "!?"
        # else:
        #     while randomPeg.isEqual(source, True) and randomPeg.isEqual(source) and randomPeg.isValid() == False and randomPeg.isEmpty():
        #         randomIndex = random.randint(0, length - 1)
        #         randomPeg = self.pegs[randomIndex]
        #         print "!"
        # print "\final random peg is"
        # print randomPeg.disksOn()
        # return randomPeg

    def nextState(self, sourcePeg, targetPeg):
        if sourcePeg.isEqual(targetPeg):
            return sourcePeg
        if sourcePeg.peek() != None:
            disk = sourcePeg.peek()
            sourcePeg.pop()

            targetPeg.push(disk)

        return self


def readStateFromFile(name):
    scriptDirectory = os.path.dirname(__file__) #<-- absolute dir the script is in
    relativePath = FILE_NAME + name
    absoluteFilePath = os.path.join(scriptDirectory, relativePath)
    configFile = open(absoluteFilePath, "r")

    pegId = 1
    pegs = list()
    for line in configFile:
        disks =  [aDisk for aDisk in [Disk(ord(weight) - 48) for weight in line if weight != "\n" and weight != "0"]]
        peg = Peg(pegId, disks)
        pegs.append(peg)
        pegId += 1
    configFile.close()

    return State(pegs)

print "initial state\n"
initialState = readStateFromFile("input.txt")
initialState.printState()

print initialState.isValid()

# # initialState.nextState(initialState.pegs[0], initialState.pegs[2])
# # initialState.printState()

# print "final state\n"
finalState = readStateFromFile("output.txt")
finalState.printState()

initialState.randomValidPeg()
# # print finalState.isEqual(initialState)

# def randomMoveFrom(state):
#     sourcePeg = state.randomValidPeg()
#     print "sourcePeg is"
#     print sourcePeg.disksOn()
#     targetPeg = state.randomValidPeg(sourcePeg)
#     print "targetPeg is"
#     print targetPeg.disksOn()
#     return (sourcePeg, targetPeg)

# i = 0;
# while initialState.isEqual(finalState) == False:
#     print "MOVE NUMBER >"
#     print i
#     sourceAndTarget = randomMoveFrom(initialState)
#     print "source and target"
#     print sourceAndTarget[0].disksOn()
#     print sourceAndTarget[1].disksOn()

#     print "\nnext state\n"

#     initialState.nextState(sourceAndTarget[0], sourceAndTarget[1])
#     initialState.printState()
#     i += 1