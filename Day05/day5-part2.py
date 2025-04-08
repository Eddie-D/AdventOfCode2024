[rules, manuals] = open('input.txt').read().split('\n\n')

manuals = [[int(x) for x in l.split(',')] for l in manuals.split('\n')]

rules = rules.split('\n')
before = [int(x.split('|')[0]) for x in rules]
after = [int(x.split('|')[1]) for x in rules]

# Add invalid manuals
invalidManuals = []
def addManualIfInvalid(m):
    for nIndex, num in enumerate(m):
        for bIndex, b in enumerate(before):
            if b == num and after[bIndex] in m:
                if m.index(after[bIndex]) < nIndex:
                    invalidManuals.append(m)
                    return

for m in manuals :
    addManualIfInvalid(m)

# While a manual is invalid, swap what makes it invalid
def swapInvalidManual(m):
    for nIndex, num in enumerate(m):
        for bIndex, b in enumerate(before):
            if b == num and after[bIndex] in m:
                if m.index(after[bIndex]) < nIndex:
                    i = m.index(after[bIndex])
                    x = m[nIndex]
                    m[nIndex] = m[i]
                    m[i] = x
                    return False
    return True

for m in invalidManuals:
    valid = False
    while(not valid):
        valid = swapInvalidManual(m)

sum = 0
for mIndex, m in enumerate(invalidManuals):
    sum += m[int((len(m)-1)/2)]
        

print(sum)