
def load_input():
    with open("input_day11.txt") as f:
        return [x for x in f.read().splitlines()]

class Game:
    def __init__(self, input, version = 1):
        self.run = True
        self.cycle = 0
        self.empty = set()
        self.occupied = set()
        self.rules = {
            0: (1, 0),
            1: (1, 1),
            2: (0, 1),
            3: (-1, 1),
            4: (-1, 0),
            5: (-1, -1),
            6: (0, -1),
            7: (1, -1)
        }
        for y, row in enumerate(input):
            for x, cell in enumerate(row):
                if cell == "L":
                    self.empty.add((x, y))
        self.boundary_x = len(input[0])
        self.boundary_y = len(input)
        self.version = version

    def advance_cycle(self):
        self.cycle += 1
        self.next_occupied = set()
        self.next_empty = set()
        for cell in self.occupied | self.empty:
            self.check_neighbors(cell) if self.version == 1 else self.check_directions(cell)
        if (self.occupied == self.next_occupied):
            print("no state change")
            print(f"cycle: {self.cycle} num_occupied: {len(self.occupied)}")
            self.run = False
        
        self.occupied = self.next_occupied
        self.empty = self.next_empty

    def check_neighbors(self, cell):
        x,y = cell
        neighbors = [(x + i, y + j) for i in (-1, 0, 1) for j in (-1, 0, 1)]
        num_occupied = 0
        for n in neighbors:
            if n == cell:
                continue
            if n in self.occupied:
                num_occupied += 1
        if cell in self.empty and num_occupied == 0:
            self.next_occupied.add(cell)
        elif cell in self.occupied and num_occupied >= 4:
            self.next_empty.add(cell)
        elif cell in self.occupied:
            self.next_occupied.add(cell)
        else:
            self.next_empty.add(cell)

    def check_directions(self, cell):
        num_occupied = 0
        for k, v in self.rules.items():
            curr = list(cell)
            while True:
                curr[0] += v[0]
                curr[1] += v[1]
                if curr[0] < 0 or curr[0] > self.boundary_x or curr[1] < 0 or curr[1] > self.boundary_y:
                    break
                elif tuple(curr) in self.occupied:
                    num_occupied += 1
                    break
                elif tuple(curr) in self.empty:
                    break
            if num_occupied >= 5:
                break
        if cell in self.occupied and num_occupied >= 5:
            self.next_empty.add(cell)
        elif cell in self.empty and num_occupied == 0:
            self.next_occupied.add(cell)
        elif cell in self.occupied:
            self.next_occupied.add(cell)
        else:
            self.next_empty.add(cell)
            

    def run_cycles(self):
        self.run = True
        while self.run:
            self.advance_cycle()

    def __str__(self):
        res = ""
        for y in range(self.boundary_y):
            for x in range(self.boundary_x):
                if (x,y) in self.occupied:
                    res += "#"
                elif (x,y) in self.empty:
                    res += "L"
                else:
                    res += "."
            res += "\n"
        return res

if __name__ == "__main__":
    input = load_input()
    game1 = Game(input)
    game1.run_cycles()

    game2 = Game(input, 2)
    game2.run_cycles()