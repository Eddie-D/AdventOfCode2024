import numpy as np

lines = open('input.txt').read().split('\n')

# Read into vars
spl = [l.split(': ') for l in lines]
test = [int(s[0]) for s in spl]
eqs = [[int(i) for i in s[1].split(' ')] for s in spl]
print(test)
print(eqs)

def mulAdd(arr, x):
    if(x < 0): print('oh no')
    if(arr.size == 0):
        return np.array([x], dtype=np.int64)
    else:
        print('x:', x)
        conc = arr * 10**len(str(x)) + x
        print('conc:', conc)
        mul = arr*x
        print('mul:', mul)
        sum = arr+x
        print('sum:', sum)
        return np.concatenate((mul,sum,conc), dtype=np.int64) 

valid = []
tot = 0
for ei, e in enumerate(eqs):
    arr = np.array([], dtype=np.int64)
    for o in e:
        arr = mulAdd(arr, o)
        print(arr)
    if(test[ei] in arr): tot += test[ei]
    valid.append(test[ei] in arr)
    # print('Test:', test[ei], arr.size, test[ei] in arr)
print(tot)

sum = 0
for vi, v in enumerate(valid):
    if v: sum += test[vi]
print(sum)
