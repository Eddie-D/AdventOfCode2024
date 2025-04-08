import re;
fileReader = open('Input.txt', 'r')
height = 0
width = 0

keyword = 'XMAS'

def  horizCount(matrix) :
    count = 0
    for h in range(height) :
        line = ''.join(matrix[h])
        count += line.count(keyword)
    return count

def downRightDiagonalCount(matrix) :
    count = 0
    for h in range(height - len(keyword) + 1) :
        for l in range(width - len(keyword) + 1) :
            diag = ''.join(matrix[h+k][l+k] for k in range(len(keyword)))
            if(diag == keyword) :
                count += 1
                print('h: ', h, 'l: ', l)
    return count

def rotate(m) :
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
            

# Pre-read to find the height and width
lines = []
for line in fileReader:
    line = line.replace('\n', '')
    lines.append(line)
    if len(line) > width : 
        width = len(line)
    height += 1

matrix = [['b' for x in range(width)] for y in range(height)] # Use b as placeholder, should make diagonals easier

fileReader = open('Input.txt')
for l in range(len(lines)):
    for c in range(len(lines[l])):
        matrix[l][c] = lines[l][c]

sum = 0
for i in range(4) :
    x = downRightDiagonalCount(matrix)
    sum += x
    print('diagonal', i, ':',x)
    sum += horizCount(matrix)
    print('Horizontal', i, ':',horizCount(matrix))
    matrix = rotate(matrix)
    t = height
    height = width
    width = t

print('Sum :', sum)