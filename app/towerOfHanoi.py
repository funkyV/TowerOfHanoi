import randomStrategy
import hcStrategy
import backtrackingStrategy
import aStarStrategy
import stateSpace

print 'Welcome to our implementation of the 4 strategies for Tower of Hanoi. '
print 'Menu'
print 'Press the number associated to each strategy to use it for the game'
print '1. Random'
print '2. Hill Climbing'
print '3. Backtracking'
print '4. A*'
print '5. Quit'

while True:
    command = raw_input()
    print 'You chose ' + command
    if command == "1":
        randomStrategy.randomHanoi("input.txt", "output.txt")
        # state = stateSpace.readStateFromFile("input.txt")
        # print state.isValid()
    elif command == "5":
        exit()
    