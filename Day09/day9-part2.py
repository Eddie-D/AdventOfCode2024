file = [int(x) for x in open('input.txt').read()]

blocks = []
for i in range(0, len(file),2):
    blocks.append({'space':False,'name':int(i/2), 'size':file[i]})
    if(i + 1 < len(file)):
        blocks.append({'space':True, 'name':0, 'size':file[i+1]})
print('Length:', len(blocks))

for i in range(len(blocks) - 1,-1,-1):
    # print('blocks:', blocks)
    if(not blocks[i]['space']) :
        for bi, b in enumerate(blocks):
            # print('bi',bi)
            if(i <= bi):
                break
            if(b['space']):
                if(b['size'] >= blocks[i]['size']):
                    print('Swapping:', blocks[i]['name'])
                    if(b['size'] != blocks[i]['size']):
                        b['size'] = b['size'] - blocks[i]['size']
                        blocks.insert(bi, blocks[i])
                    else:
                        blocks[bi] = blocks[i]
                    print('post-swap')
                    print(blocks[i])

                    blocks[i] = {'space':True,'name':0,'size':blocks[i]['size']}
                    print(blocks[i])
                    break                    

print('End blocks',blocks)
arr = []
for b in blocks:
    for x in range(b['size']):
        arr.append(b['name'])


print('Length:', len(blocks))
print(blocks)
print(arr)