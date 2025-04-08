import numpy as np
map = [[c for c in l] for l in open('input.txt').read().split('\n')]
height = len(map)
width = len(map[0])
scores = [[-1 for w in range(width)] for h in range(height)]

start = np.array((0,0))
for li, l in enumerate(map):
    for ci, c in enumerate(l):
        if c == 'S':
            start = np.array((li,ci))
        
def charAt(loc):
    return map[loc[0]][loc[1]]
def setLowerScore(loc, score):
    if scores[loc[0]][loc[1]] > score or scores[loc[0]][loc[1]] == -1:
        scores[loc[0]][loc[1]] = score
        return True
    return False

def checkNext(loc, dir, score, first=False):
    proceed = setLowerScore(loc, score)
    if(charAt(loc) == '#' or charAt(loc) == 'E' or not proceed):
        return
    checkNext(loc + dir, dir, score + 1)
    cwDir = np.array((dir[1], -dir[0]))
    checkNext(loc + cwDir,cwDir, score + 1001)
    acwDir = np.array((-dir[1], dir[0]))
    checkNext(loc + acwDir, acwDir, score + 1001)
    if(first):
        checkNext(loc -dir, np.array((0,0)) - dir, score + 2002)

def printMap():
    str = ''
    for l in map:
        for c in l:
            str += c + ' '
        str += '\n'
    print('Map:', str)
def printScores():
    string = ''
    for l in scores:
        for c in l:
            string += str(c) + ' '
        string += '\n'
    print('Scores:', string)


checkNext(start, np.array((0,1)), 0, True)

print('End score')
endScore = -1
for li, l in enumerate(map):
    for ci, c in enumerate(l):
        if(c == 'E'):
            endScore = scores[li][ci]

print('Lowest Score:', endScore)
