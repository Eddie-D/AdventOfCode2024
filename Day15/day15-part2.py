import numpy as np
file = open('input.txt').read().split('\n\n')

map = [[c for c in l] for l in file[0].split('\n')]
strMoves = file[1].replace('\n','')
moves = []
for s in strMoves:
    match s:
        case '^':
            moves.append(np.array((-1,0)))
        case 'v':
            moves.append(np.array((1,0)))
        case '>':
            moves.append(np.array((0,1)))
        case '<':
            moves.append(np.array((0,-1)))

robot = np.array((0,0))
for li, l in enumerate(map):
    for ci, c in enumerate(l):
        if(c == '@'):
            robot = np.array((li,ci))

def printMap():
    s = ''
    for l in map:
        for c in l:
            s += c
        s += '\n'
    print(s)

def atPos(pos):
    return map[pos[0]][pos[1]]
def setPos(pos, c):
    map[pos[0]][pos[1]] = c
def vertical(dir):
    return dir[0] != 0

def canMove(pos, dir):
    # Some points will be checked twice (or more), but c'est la vie
    if(vertical(dir)):
        if(atPos(pos) == '['):
            return canMove(pos + dir, dir) and canMove(pos + dir + np.array((0,1)), dir)
        if(atPos(pos) == ']'):
            return canMove(pos + dir, dir) and canMove(pos + dir + np.array((0,-1)), dir)

    if(atPos(pos) == '.'):
        return True
    if(atPos(pos) == '#'):
        return False
    return canMove(pos + dir, dir)

# Wierd stuff will happein if consecutive boxes, but *should* be fine
def move(pos,dir):
    if(atPos(pos) == '['):
        move(pos + np.array(0,1),dir)
        setPos(pos + np.array(0,1), '.')
    if(atPos(pos) == ']'):
        move(pos + np.array(0,-1),dir)
        setPos(pos + np.array(0,-1), '.')
    
    setPos(pos + dir, atPos(pos))
    if(atPos(pos) == '@'):
        setPos(pos, '.')

for m in moves:
    if(canMove(robot, m)):
        move(robot, m)
        robot += m
    printMap()

printMap()

total = 0
for li, l in enumerate(map):
    for ci, c in enumerate(l):
        if(c == 'O'):
            total += li * 100 + ci
print('Total:', total)