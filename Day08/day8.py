import numpy as np
import matplotlib.pyplot
import math
matrix = [[c for c in l]for l in open('input.txt').read().split('\n')]

height = len(matrix)
width = len(matrix[0])

chars = {} # Dictionary
for li, l in enumerate(matrix):
    for ci, c in enumerate(l):
        if(c != '.'):
            if(not c in chars):
                chars[c] = []
            chars[c].append(np.array((li,ci)))

nodes = {}
def addNodeIfValid(node):
    if(0 <= node[0] and node[0] < height and 0 <= node[1] and node[1] < width):
        nodes[str(node)] = node
        return True
    return False

def addNodes(arr):
    for i, loc1 in enumerate(arr):
        for j, loc2 in enumerate(arr[i+1:]):
            dist = loc2 - loc1
            dist = np.array([int(d) for d in dist / math.gcd(dist[0], dist[1])])
            print(loc1,':',loc1[0],loc1[1])
            l1 = np.array((loc1[0], loc1[1]))
            
            while(addNodeIfValid(loc1 - dist)):
                loc1 -= dist

            while(addNodeIfValid(l1 + dist)):
                l1 += dist
                print(dist)
                print(l1)

def printChars():
    m = [['.' for x in l] for l in matrix]

    for key in chars:
        for pair in chars[key]:
            print('p:', pair[0])
            m[pair[0]][pair[1]] = key

    s = ''
    for l in m:
        for c in l:
            s += c
        s += '\n'
    print('m:\n', s)

for i in chars:
    addNodes(chars[i])

sum = 0
for node in nodes:
    sum += 1

print(nodes)
printChars()
print('Sum:', sum)