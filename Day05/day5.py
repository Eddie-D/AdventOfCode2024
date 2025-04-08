[rules, manuals] = open('input.txt').read().split('\n\n')

manuals = [[int(x) for x in l.split(',')] for l in manuals.split('\n')]

rules = rules.split('\n')
before = [int(x.split('|')[0]) for x in rules]
after = [int(x.split('|')[1]) for x in rules]

# Set manuals valid to begin
validManuals = [1 for x in manuals]

for mIndex, m in enumerate(manuals) :
    for nIndex, num in enumerate(m):
        for bIndex, b in enumerate(before):
            if b == num and after[bIndex] in m:
                if m.index(after[bIndex]) < nIndex:
                    validManuals[mIndex] = 0

print(validManuals)

# Sum middles
sum = 0
for mIndex, m in enumerate(manuals):
    if validManuals[mIndex] == 1:
        sum += m[int((len(m)-1)/2)]

print('Sum :', sum)
