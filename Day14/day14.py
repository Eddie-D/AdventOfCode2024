import re
import numpy as np
file = open('input.txt').read().split('\n')
dimensions = np.array([101,103])

robots = []
for l in file:
    robots.append({
        'p': np.array([int(x) for x in re.search('(?<=p=)(-?\d*),(-?\d*)', l).groups()]),
        'v': np.array([int(x) for x in re.search('(?<=v=)(-?\d*),(-?\d*)', l).groups()])
    })

for count in range(100000):
    positions = []
    for r in robots:
        positions.append(np.mod(r['p'] + r['v']*count, dimensions))

    quadrants = [[0,0],[0,0]]
    for p in positions:
        quad = (p - ((dimensions - np.array([1,1])) / 2))
        if(quad[0] < 0 and quad[1] < 0): quadrants[0][0] += 1
        if(quad[0] > 0 and quad[1] < 0): quadrants[1][0] += 1
        if(quad[0] < 0 and quad[1] > 0): quadrants[0][1] += 1
        if(quad[0] > 0 and quad[1] > 0): quadrants[1][1] += 1

    sum = 1
    for h in quadrants:
        for q in h:
            sum *= q

    def printIfViableImage():
        likelihood = 0
        im = [['.' for w in range(dimensions[0])]for l in range(dimensions[1])]
        for p in positions:
            im[p[1]][p[0]] = '*'
        s = ''
        for l in im:
            consec = 0
            for c in l:
                s += c
                if(c == '*'):
                    consec += 1
                else:
                    likelihood += consec**2
                    consec = 0
                likelihood += consec**2
            s += '\n'
        if(likelihood > 1200):
            print('Count:',count,'likelihood:',likelihood,'image')
            print(s)
            #print('Positions:',positions)

    printIfViableImage()