file = [int(x) for x in open('input.txt').read()]

list = []
for i in range(0, len(file),2):
    for j in range(file[i]):
        list.append(int(i/2))
    if(i + 1 < len(file)):
        for k in range(file[i+1]):
            list.append(-1)

iEmpty = 0
iFull = len(list) - 1
for i in range(len(list)-1, -1, -1):
    # Find next empty
    while(iEmpty < len(list) and list[iEmpty] != -1):
        iEmpty += 1
    # Find next full 
    while(iFull >= 0 and list[iFull] == -1):
        iFull -= 1
    
    if(iEmpty >= iFull):
        break
    else:
        list[iEmpty] = list[iFull]
        list[iFull] = -1

# Remove -1 from end
while(list[-1] == -1):
    list.pop()

sum = 0
for li, l in enumerate(list):
    sum += l*li

print('Sum:', sum)