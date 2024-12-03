import re

def part1(section) : 
    mults = re.findall('mul\(\d\d?\d?,\d\d?\d?\)',section)

    sum = 0
    for str in mults : 
        [num1, num2] = re.findall('\d\d?\d?,\d\d?\d?', str)[0].split(',')
        sum += int(num1) * int(num2)

    return sum

def part2(input) :
    doSections = list(filter(None, re.split("do(?!(n't))", input)))
    multSections = [sec.split("don't")[0] for sec in doSections]
    sum = 0
    for sec in multSections :
        sum += part1(sec)

    return sum

input = open('Input.txt', 'r').read()
print('Sum 1:', part1(input))
print('Sum 2:', part2(input))