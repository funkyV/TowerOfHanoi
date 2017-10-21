import randomStrategy
import hcStrategy
import backtrackingStrategy
import aStarStrategy

print 'Welcome to our implementation of the 4 strategies for Tower of Hanoi. '
print 'Menu'
print 'Press the number associated to each strategy to use it for the game'
print '1. Random'
print '2. Hill Climbing'
print '3. Backtracking'
print '4. A*'

while True:
    a = raw_input()
    print 'You chose ' + a
    