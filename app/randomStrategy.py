import stateSpace

def randomMoveFrom(state):
    ok = False
    while ok == False:
        sourcePeg = state.randomValidPeg()

        # while sourcePeg.isValid() == False or sourcePeg.isEmpty() == True:
            # sourcePeg = state.randomValidPeg()

        targetPeg = state.randomValidPeg()

        # while targetPeg.isValid() == False or sourcePeg.isEqual(targetPeg) == True:
            # targetPeg = state.randomValidPeg()

        if sourcePeg.peek() != None:
            if targetPeg.peek() == None:
                ok = True
            else:
                if sourcePeg.peek().weight < targetPeg.peek().weight:
                    ok = True
    return (sourcePeg, targetPeg)

def randomHanoi(inputFileName, outputFileName):
    print "initial state\n"
    initialState = stateSpace.readStateFromFile(inputFileName);
    initialState.printState()

    if initialState.isValid() == False:
        print "input state is not valid"
        exit()
    # initialState.nextState(initialState.pegs[0], initialState.pegs[2])
    # initialState.printState()

    print "\nfinal state\n"
    finalState = stateSpace.readStateFromFile(outputFileName);
    finalState.printState()
    if finalState.isValid() == False:
        print "final state is not valid"
        exit()

    i = 0

    while initialState.isEqual(finalState) == False:
        print "current state\n"
        initialState.printState()

        sourceAndTarget = randomMoveFrom(initialState)

        initialState.nextState(sourceAndTarget[0], sourceAndTarget[1])

        print "MOVE NUMBER >"
        print i
        print "\n"

        i += 1
    initialState.printState()