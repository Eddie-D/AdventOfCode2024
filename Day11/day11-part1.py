import itertools

stones = [int(s) for s in open('input.txt').read().split(' ')]

for b in range(10):
    print(b, 'blinks:')

    for si, s in enumerate(stones):
        if s == 0:
            stones[si] = [1]
        elif len(str(s)) % 2 == 0:
            half = int(len(str(s))/2)
            stones[si] = [int(str(s)[:half]), int(str(s)[half:])]
        else:
            stones[si] = [s*2024]

    # Unflatten array
    newStones = []
    for s in stones:
        for x in s:
            newStones.append(x)
    stones = newStones
    
    newUsed = {}
    for x in stones:
        newUsed[x] = True
    newUsed = sorted(newUsed)
    s = ''
    for u in newUsed:
        s+= str(u) + ' '
    
    print('Used length:', len(newUsed))
    print('Used stones:', s)
    # print()
    print('Stone length:', len(stones))