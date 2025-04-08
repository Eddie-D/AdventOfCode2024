import math
file = open('input.txt').read().split('\n')

ip = 0
a = int(file[0][12:])
b = int(file[1][12:])
c = int(file[2][12:])
initProgram = [int(n) for n in file[4][9:].split(',')]
stA = ''
for p in initProgram:
    stA += str(p)
a = stA
program = [p for p in initProgram].reverse()

# Padding with any 1's will only result in a bigger final number (I think)


