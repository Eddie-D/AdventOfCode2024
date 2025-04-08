import sys
# This is probably not a great idea
sys.setrecursionlimit(10000)

# Input variables
sideLength = 71
truncLength = 1024

# Print methods
def printDotHashSpace(space):
    string = ''
    for l in space:
        for x in l:
            string += '.' if x != -1 else '#'
        string += '\n'
    print(string)

def printNumSpace(space):
    string = ''
    for l in space:
        for x in l:
            string += str(x) + ' '
        string += '\n'
    print(string)


# Create matrix
reasonableMax = sideLength ** 2 + 1
space = [[reasonableMax for x in range(sideLength)] for y in range(sideLength)]

# Read and truncate file
file = open('input.txt').read().split('\n')
file = [file[i] for i in range(truncLength)]

for l in file:
    coord = l.split(',')
    space[int(coord[1])][int(coord[0])] = -1
    # Assumes the final space is not blocked

# Start in corner and navigate in all directions recursively
def recursiveDirectionNav(x,y, currentStep):
    if(0 <= x and x < sideLength and 0 <= y and y < sideLength and space[x][y] > currentStep + 1):
        space[x][y] = currentStep
        currentStep += 1
        recursiveDirectionNav(x-1, y, currentStep)
        recursiveDirectionNav(x+1, y, currentStep)
        recursiveDirectionNav(x, y-1, currentStep)
        recursiveDirectionNav(x, y+1, currentStep)

recursiveDirectionNav(0,0,0)
printNumSpace(space)
print('The minimum number of spaces is:', space[sideLength-1][sideLength-1])