file = [[c for c in l] for l in open('input.txt').read().split('\n')]

class Plot:
    def __init__(self, char):
        self.coordinates = {}
        self.char = char

    def contains(self, coord, char):
        return char == self.char and coord in self.coordinates

    def touches(self, coord, char):
        if(char != self.char):
            return False
        inGroup = False
        # Up
        inGroup = inGroup or (coord[0] - 1, coord[1]) in self.coordinates
        # Down
        inGroup = inGroup or (coord[0] + 1, coord[1]) in self.coordinates
        # Left
        inGroup = inGroup or (coord[0], coord[1] - 1) in self.coordinates
        # Right
        inGroup = inGroup or (coord[0], coord[1] + 1) in self.coordinates

        return inGroup

    def add(self,coord):
         self.coordinates[coord] = True 
    
    def __str__(self):
        s = ''
        for c in self.coordinates:
            s += str(c) + ','
        return s

    def area(self):
        return len(self.coordinates)

    def perim(self):
        perim = 0
        for coord in self.coordinates:
            perim += 4
            # Up
            if((coord[0] - 1, coord[1]) in self.coordinates): perim -= 1
            # Down
            if((coord[0] + 1, coord[1]) in self.coordinates): perim -= 1
            # Left
            if((coord[0], coord[1] - 1) in self.coordinates): perim -= 1
            # Right
            if((coord[0], coord[1] + 1) in self.coordinates): perim -= 1
        return perim
    
    def sides(self):
        # Unfortunately, flawed in concept
        outer = []
        for coord in self.coordinates:
            outer.append((coord[0] - 1, coord[1]))
            outer.append((coord[0] + 1, coord[1]))
            outer.append((coord[0], coord[1] - 1))
            outer.append((coord[0], coord[1] + 1))
        
        for s in self.coordinates:
            outer = [x for x in outer if x != s]
            
        plots = []
        for coord in outer:
            inPlots = []
            for p in plots:
                if(p.touches(coord,'x')):
                    inPlots.append(p)
            if(len(inPlots) == 0):
                new = Plot('x')
                new.add(coord)
                plots.append(new)
            elif(len(inPlots) == 1):
                inPlots[0].add(coord)
            else:
                plots.append(mergePlots(inPlots, coord))
                for ip in inPlots:
                    plots.remove(ip)
        # print([str(p) for p in plots])
        return len(plots)



def mergePlots(plots, add):
    plot = Plot(plots[0].char)
    for p in plots:
        for c in p.coordinates:
            plot.add(c)
    plot.add(add)
    return plot                                  

plots = []
for li, l in enumerate(file):
    for ci, c in enumerate(l):
        inPlots = []
        for pi, p in enumerate(plots):
            if(p.touches((li,ci),c)):
                inPlots.append(p)
        if(len(inPlots) == 0):
            new = Plot(c)
            new.add((li,ci))
            plots.append(new)
        elif(len(inPlots) == 1):
            inPlots[0].add((li,ci))
        else:
            plots.append(mergePlots(inPlots, (li,ci)))
            for ip in inPlots:
                plots.remove(ip)

print('Len(plots):', len(plots))
sum = 0
for p in plots:
    print('Sides:', p.sides(), 'area:', p.area())
    sum += p.sides() * p.area()

print('Sum:', sum)