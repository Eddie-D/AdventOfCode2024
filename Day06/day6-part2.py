import os
# Read input and convert to multidimensional array
oinput = [[c for c in l] for l in open('input.txt').read().split('\n')]
matrix = [[c for c in l] for l in oinput]

dir = [-1, 0]   # Origin is at top right and down and right are positive to match indicies
loc = [0, 0]

# Find location
for li, l in enumerate(matrix):
    for ci, c in enumerate(l):
        if c == '^':
            loc = [li, ci]
# print('Location:', loc)

width = len(matrix)
height = len(matrix[0])

# For debugging
def prettyPrint(input):
    s = ''
    for l in input:
        for c in l :
            s += c
        s+= '\n'
    print(s)

# Use part 1 to find intial viable positions and mark X
def markX(input, loc, dir):
    while(0 <= loc[0] and loc[0] < height and 0 <= loc[1] and loc[1] < width) :
        input[loc[0]][loc[1]] = 'X'
        while (loc[0] + dir[0] < height and loc[0] + dir[0] < width and input[loc[0] + dir[0]][loc[1] + dir[1]] == '#'):
            # Rotate clockwise
            dir[0] = dir[0] + dir[1]
            dir[1] = dir[1] - dir[0]
            dir[0] = dir[0] + dir[1]
        loc = [loc[0] + dir[0], loc[1] + dir[1]]
    return input

def isLoop(input, loc, dir):
    # print('h:', height)
    while(0 <= loc[0] and loc[0] < height and 0 <= loc[1] and loc[1] < width) :
        if input[loc[0]][loc[1]] != 'R': input[loc[0]][loc[1]] = 'X'
        # print('Loc:',loc,'Dir', dir)
        # prettyPrint(input)
        if (0 <= loc[0] + dir[0] and loc[0] + dir[0] < height and 0 <= loc[1] + dir[1] and loc[1] + dir[1] < width and input[loc[0] + dir[0]][loc[1] + dir[1]] == '#'):
            if(input[loc[0]][loc[1]] == 'R'):
                # print('Loc:',loc,'Dir', dir)
                return True
            input[loc[0]][loc[1]] = 'R'
            while (loc[0] + dir[0] < height and loc[1] + dir[1] < width and input[loc[0] + dir[0]][loc[1] + dir[1]] == '#'):
                # Repeatedly rotate clockwise
                dir[0] = dir[0] + dir[1]
                dir[1] = dir[1] - dir[0]
                dir[0] = dir[0] + dir[1]
        loc = [loc[0] + dir[0], loc[1] + dir[1]]
    # print('Loc:',loc,'Dir', dir)
    return False

matrix = markX(matrix, [loc[0], loc[1]], [dir[0], dir[1]])
# prettyPrint(matrix)
sum = 0
for li, l in enumerate(matrix):
    for ci, c in enumerate(l):
        if(c == 'X'):
            
            cop = [[c for c in l] for l in oinput]
            cop[li][ci] = '#'
            if(isLoop(cop, [loc[0], loc[1]], [dir[0],dir[1]])): 
                sum += 1
                # print('Looped')
            # else: 
                # print('Escaped')
            # print('Manuals: l:', li, 'c:', ci)

print('Sum:', sum)