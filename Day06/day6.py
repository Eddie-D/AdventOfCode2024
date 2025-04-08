# Read input and convert to multidimensional array
input = [[c for c in l] for l in open('input.txt').read().split('\n')]

dir = [-1, 0]   # Origin is at top right and down and right are positive to match indicies
loc = [0, 0]

# Find location
for li, l in enumerate(input):
    for ci, c in enumerate(l):
        if c == '^':
            loc = [li, ci]

width = len(input)
height = len(input[0])

print(width)
print(height)
while(0 <= loc[0] and loc[0] < height and 0 <= loc[1] and loc[1] < width) :
    input[loc[0]][loc[1]] = 'X'
    while (loc[0] + dir[0] < height and loc[1] + dir[1] < width and input[loc[0] + dir[0]][loc[1] + dir[1]] == '#'):
        # Rotate clockwise
        dir[0] = dir[0] + dir[1]
        dir[1] = dir[1] - dir[0]
        dir[0] = dir[0] + dir[1]
    loc = [loc[0] + dir[0], loc[1] + dir[1]]

sum = 0
for l in input:
    for c in l:
        if(c == 'X'): sum += 1
print('Sum:', sum)