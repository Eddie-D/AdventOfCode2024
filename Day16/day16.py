import numpy as np
map = [[c for c in l] for l in open('input.txt').read().split('\n')]
height = len(map)
width = len(map[0])
scores = [[-1 for w in range(width)] for h in range(height)]

bestEnd = -1
finishing = []
start = np.array((0,0))
for li, l in enumerate(map):
    for ci, c in enumerate(l):
        if c == 'S':
            start = np.array((li,ci))
        
def charAt(loc):
    return map[loc[0]][loc[1]]
def setLowerScore(loc, score):
    if scores[loc[0]][loc[1]] >= score or scores[loc[0]][loc[1]] == -1:
        scores[loc[0]][loc[1]] = score
        return True
    elif score - scores[loc[0]][loc[1]] < 1001:
        return True
    return False
def inFinishing(loc):
        for f in finishing:
            if ((f == loc).all()):
                return True
        return False

toCheck = []
def check(params, first=False):
    loc, dir, score, path = params
    proceed = setLowerScore(loc, score)
    if(charAt(loc) == '#' or not proceed):
        return
    if(charAt(loc) == 'E'):
        global bestEnd
        global finishing
        if(score == bestEnd):
            print('Score tied best: ', bestEnd)
            for p in path:
                if not inFinishing(p):
                    finishing.append(p)
        elif(bestEnd == -1 or score < bestEnd):
            print('Old best:', bestEnd, 'New best', score)
            finishing = [p for p in path]
            bestEnd = score
    path = path.copy()
    path.append(loc)
    toCheck.append([loc + dir, dir, score + 1, path])
    cwDir = np.array((dir[1], -dir[0]))
    toCheck.append([loc + cwDir,cwDir, score + 1001, path])
    acwDir = np.array((-dir[1], dir[0]))
    toCheck.append([loc + acwDir, acwDir, score + 1001, path])
    if(first):
        toCheck.append([loc -dir, np.array((0,0)) - dir, score + 2002, path])

def printMap():
    copyMap = [[c for c in l] for l in map]
    for v in finishing:
        copyMap[v[0]][v[1]] ='o' 
    str = ''
    for li, l in enumerate(copyMap):
        for ci, c in enumerate(l):
            str += c
        str += '\n'
    print('Map:', str)
def printScores():
    string = ''
    for l in scores:
        for c in l:
            string += str(c) + ' '
        string += '\n'
    print('Scores:', string)


check([start, np.array((0,1)), 0, []], True)
while(len(toCheck) != 0):
    check(toCheck[0])
    toCheck.pop(0)

printMap()

printScores()

print('Lowest Score:', bestEnd)
print('Number Seats:', len(finishing) + 1)
