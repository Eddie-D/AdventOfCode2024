file = [int(s) for s in open('input.txt').read().split(' ')]

class Stones():
    def __init__(self):
        self.stones = {}

    # Num stored as string, quantity stored as int
    def addStones(self,num,quantity):
        # print('Adding:', num, 'Quantity:', quantity)
        num = str(num)
        if(num in self.stones):
            # print('Already has:', num)
            self.stones[num] = quantity + int(self.stones[num])
        else:
            self.stones[num] = quantity
    
    def blink(self):
        # print('Blinking')
        newStones = Stones()
        # print('New stones:', newStones)
        for num, quantity in self.stones.items():
            # print('For',num,quantity)
            if num == '0':
                # print('Number zero', num)
                newStones.addStones(1, quantity)
            elif len(num) % 2 == 0:
                # print('Number even', num)
                half = int(len(num)/2)
                # print('First half:', int(num[:half]))
                newStones.addStones(int(num[:half]), quantity)
                newStones.addStones(int(num[half:]), quantity)
            else:
                newStones.addStones(int(num) * 2024, quantity)
                pass
        return newStones
    
    def numStones(self):
        sum = 0
        for k in self.stones:
            sum += self.stones[k]
        return sum
    
    def __str__(self):
        st = ''
        for s in self.stones:
            st += '(' + s + ' ' + str(self.stones[s]) + ') '
        return st

stones = Stones()
# print('Initial stones:', stones)
# print(file)
for s in file:
    stones.addStones(s,1)

for i in range(75):
    # print('Blinked', i+1)
    stones = stones.blink()
    # print('All stones:', stones)
print('Num stones:', stones.numStones())
