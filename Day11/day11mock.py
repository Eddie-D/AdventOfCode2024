class StoneManager:
    stones = []
    observing = 0

    def __init__(self, arr):
        for a in arr:
            self.stones.append(Stone(a, self))

    def __str__(self):
        string = ''
        for s in self.stones:
            string += str(s) + ' '
        return string

    def splitInto(self, stoneId, first, second):
        self.stones[stoneId] = Stone(first, self)
        self.stones.insert(stoneId + 1, Stone(second, self))
        for i in range(stoneId + 2, len(self.stones)):
            self.stones[i].setId(i)
        self.observing += 1
    
    def blink(self):
        self.observing = 0
        for self.observing, s in enumerate(self.stones):
            s.blink(self.observing)

 
class Stone:
    num:0
    def __init__(self, num, manager):
        self.num = num
        self.manager = manager

    def __str__(self):
        return str(self.num)
    
    def blink(self, id):
        if self.num == 0:
            self.num = 1
        elif len(str(self.num)) % 2 == 0:
            half = int(len(str(self.num))/2)
            print(int(str(self.num)[half:]))
            self.manager.splitInto(id, int(str(self.num)[:half]), int(str(self.num)[half:]))
        else :
            self.num *= 2024

sm = StoneManager(open('input.txt').read().split(' '))
print(sm)

sm.blink()
print(sm)