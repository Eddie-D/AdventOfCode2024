import re;
fileReader = open('Input.txt', 'r')
height = 0
width = 0

# Pre-read to find the height and width
lines = []
for line in fileReader:
    line = line.replace('\n', '')
    lines.append(line)
    if len(line) > width : 
        width = len(line)
    height += 1

matrix = [['b' for x in range(width)] for y in range(height)] # Use b as placeholder, should make diagonals easier

a = []
fileReader = open('Input.txt')
for l in range(len(lines)):
    for c in range(len(lines[l])):
        # Find a's that aren't in the outer ring of text
        if(lines[l][c] == 'A' and l > 0 and l < width-1 and c > 0 and c < width-1): a.append([l,c])
        matrix[l][c] = lines[l][c]

sum = 0
for x in a:
    diag1 = matrix[x[0]-1][x[1]-1] + matrix[x[0]][x[1]] + matrix[x[0]+1][x[1]+1]
    diag2 = matrix[x[0]+1][x[1]-1] + matrix[x[0]][x[1]] + matrix[x[0]-1][x[1]+1]
    if((diag1 == 'MAS' or diag1 == 'SAM') and (diag2 == 'MAS' or diag2 == 'SAM')): sum += 1

print(sum)
