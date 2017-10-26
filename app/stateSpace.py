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

        if length <= 1:
            return True
        if len(self.items) % 2 != 0:
            return self.items[length].weight < self.items[length - 1].weight

        for i in range(length):
            twoDisks = self.items[i : i+2]
            if twoDisks[0] < twoDisks[1]:
                return False

class Disk:
    def __init__(self, weight):
        self.weight = weight

class State:
    def __init__(self, pegs):
        self.pegs = pegs

    def printState(self):
        print "STATE"
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
    def randomValidPeg(self, source = None):   
        length = len(self.pegs) - 1

        randomIndex = random.randint(0, length)
        randomPeg = self.pegs[randomIndex]
        print "prima data"
        print randomIndex
        if source == None:
            condition = randomPeg.isEmpty()
            print ("conditie 1")
        else:
            condition = randomPeg.isEmpty() and randomPeg.isEqual(source, True)
            print ("conditie 2")
        while condition :
            print "In loop"
            randomIndex = random.randint(0, length)
            randomPeg = self.pegs[randomIndex]

            if source == None:
                condition = randomPeg.isEmpty()
                print ("conditie 1")
            else:
                condition = randomPeg.isEmpty() and randomPeg.isEqual(source, True)
                print ("conditie 2")

            print randomIndex

        return randomPeg

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



# print initialState.isValid()

# initialState.nextState(initialState.pegs[0], initialState.pegs[2])
# initialState.printState()

# finalState = readStateFromFile("output.txt")
# finalState.printState()

# print finalState.isEqual(initialState)

def randomMoveFrom(state):
    sourcePeg = state.randomValidPeg()
    # return sourcePeg.disksOn()
    targetPeg = state.randomValidPeg(sourcePeg)

    print sourcePeg.disksOn()
    print targetPeg.disksOn()
    # return (sourcePeg, targetPeg)
# def solveHanoi(initialState, finalState):
#     currentState = initialState
#     while not currentState.isEqual(finalState):


# test
print "god help us"
randomMoveFrom(initialState)
# test

# print "blabls"
# sourceAndTarget = randomMoveFrom(initialState)
# print "source and target"
# print sourceAndTarget[0].disksOn()
# print sourceAndTarget[1].disksOn()

# print "\nnext state\n"

# initialState.nextState(sourceAndTarget[0], sourceAndTarget[1])
# initialState.printState()