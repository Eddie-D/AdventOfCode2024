import re
from sympy import Symbol, linsolve, Matrix 
unParsed = [m.split('\n') for m in open('input.txt').read().split('\n\n')]

machines = []
def findXY(line):
    re.search('X=?([+-]?\d*).*Y=?([+-]?\d*)', line).groups()
    return [int(i) for i in re.search('X=?([+-]?\d*).*Y=?([+-]?\d*)', line).groups()]

def main():
    for p in unParsed:
        machines.append({
            'a': findXY(p[0]),
            'b': findXY(p[1]),
            'p': [10000000000000 + x for x in findXY(p[2])]
        })
def part1():
    sum = 0
    answers = []
    a = Symbol('a')
    b = Symbol('b')
    for m in machines:
        answer = list(linsolve([Matrix([m['a'], m['b']]).transpose(), Matrix(m['p'])], [a,b]))[0]
        print('answer', answer)
        notInt = False
        for x in answer:
            notInt = notInt or not x.is_integer
        if(not notInt):
            answers.append(answer)
    print(answers)
    for ans in answers:
        sum += ans[0]*3 + ans[1]

    print('Sum:', sum)

main()
part1()