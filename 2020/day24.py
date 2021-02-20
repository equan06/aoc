directions = {
    "ne": (1, 0, -1),
    "nw": (0, 1, -1),
    "se": (0, -1, 1),
    "sw": (-1, 0, 1),
    "w": (-1, 1, 0),
    "e": (1, -1, 0) 
}

class HexGame:

    def __init__(self, flipped):
        self.flipped = flipped
        self.num_flipped = len(flipped)

    def check_neighbors(self, cell):
        nn = 0
        is_flipped = cell in self.flipped
        for d in directions.values():
            n = move(cell, d)
            if n in self.flipped:
                nn += 1
            if is_flipped:
                self.to_check.add(n)
        return nn

    def cycle(self, num_iter):
        for i in range(num_iter):
            self.to_check = set()
            self.next_flipped = self.flipped.copy()
            for tile in self.flipped: # black tiles
                nn = self.check_neighbors(tile)
                if nn == 0 or nn > 2:
                    self.next_flipped.remove(tile)
            for tile in self.to_check - self.flipped: # white tiles
                nn = self.check_neighbors(tile)
                if nn == 2:
                    self.next_flipped.add(tile)
            self.flipped = self.next_flipped
            self.num_flipped = len(self.flipped)

def load_input():
    with open("input_day24.txt") as f:
        return [x for x in f.read().splitlines()]

def day24_pt1(input):
    ins = parse_input(input)
    return len(init_flipped(ins))
    
def day24_pt2(input, num_iter=100):
    g = HexGame(init_flipped(parse_input(input)))
    g.cycle(num_iter)
    return g.num_flipped

def parse_input(input):
    all_ins = []
    for line in input:
        i = 0
        ins = []
        while i < len(line):
            curr = line[i:i+2]
            if curr in directions:
                ins.append(directions[curr])
                i += 2
            else:
                ins.append(directions[line[i]])
                i += 1
        all_ins.append(ins)
    return all_ins

def init_flipped(ins):
    flipped = set()
    for line in ins:
        curr = (0, 0, 0)
        for direction in line:
            curr = move(curr, direction)
        if curr in flipped:
            flipped.remove(curr)
        else:
            flipped.add(curr)
    return flipped

def move(old, dirs):
    return tuple([old[i] + dirs[i] for i in range(3)])

if __name__ == "__main__":
    input = load_input()
    print(day24_pt1(input))
    print(day24_pt2(input))