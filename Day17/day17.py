import math
file = open('input.txt').read().split('\n')

a = int(file[0][12:])
b = int(file[1][12:])
c = int(file[2][12:])
initProgram = [int(n) for n in file[4][9:].split(',')]
output = []
print(initProgram)
outLength = 0

currentA = 0
while output != initProgram:
    print('Input:', "{0:b}".format(currentA))
    print('Output:', output)
    currentA += 1
    a = currentA
    b = 0
    c = 0
    ip = 0
    program = [p for p in initProgram]
    output = []

    def getCombo(lit):
        if lit < 4:
            return lit
        match lit:
            case 4:
                return a
            case 5:
                return b
            case 6:
                return c

    def adv(inp):
        global a
        a = a >> inp
    def bxl(inp):
        global b
        b= b ^ inp
    def bst(inp):
        global b
        b = (inp & 4) + (inp & 2) + (inp & 1)
    def jnz(inp):
        global a, ip
        if a != 0:
            ip = inp - 2
    def bxc(inp):
        global b, c
        b = b ^ c
    def out(inp):
        global output
        output.append((inp & 4) + (inp & 2) + (inp & 1))
    def bdv(inp):
        global a,b
        b = a >> inp
    def cdv(inp):
        global a,c
        c = a >> inp

    while ip < len(program) - 1:
        lit = program[ip + 1]
        cmb = getCombo(lit)
        match program[ip]:
            case 0:
                adv(cmb)
            case 1:
                bxl(lit)
            case 2:
                bst(cmb)
            case 3:
                jnz(lit)
            case 4:
                bxc(0)
            case 5:
                out(cmb)
            case 6:
                bdv(cmb)
            case 7:
                cdv(cmb)
        ip += 2

outputStr = str(output[0])
for o in output[1:]:
    outputStr  += ',' + str(o)
print('Output:', outputStr)  
print('Successful A:', currentA)