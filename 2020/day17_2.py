import itertools

"""
This is v2 of day17, as v1 was a bit of an exercise in OOP.
In 4D, it runs nearly 12x faster (<1s vs 10s) than v1!
"""

def load_input():
    with open("input_day17.txt") as f:
        return [x for x in f.read().splitlines()]


class Game:
    def __init__(self, input, dimension=3):
        if (dimension < 2):
            print("Dimension must be at least 2.")
            return 
        self.active = set()
        self.next_active = set()
        self.dimension = dimension
        self.init_inputs(input)
        self.cycle = 0

    # Store active cells in a set     
    def init_inputs(self, input):
        for y, row in enumerate(input):
            for x, val in enumerate(row):
                if val == "#":
                    self.active.add(tuple([x,y]+[0 for _ in range(self.dimension - 2)]))
        print(f"init num_active: {len(self.active)}")
        
    def advance_cycle(self):
        self.next_active = set() # clear buffer for the next cycle
        checked = set() 
        to_check = set() 
        # Check all active cells
        for coords in self.active:
            self.check_coords(coords, checked, to_check)
        # Check the neighbors of all active cells
        for coords in to_check:
            self.check_coords(coords, checked, to_check)

        self.active = self.next_active
        self.next_active = set()
        self.cycle += 1
        print(f"cycle: {self.cycle} num_active: {len(self.active)}")
        
    def check_coords(self, coords, checked, to_check):
        if coords in checked:
            return
        checked.add(coords)
        is_active = coords in self.active
        neighbors = list(itertools.product(*[[coord + i for i in (-1, 0, 1)] for coord in coords]))
        # Neighbors contains the current coord, so subtract 1 if the current cell is active
        num_active = sum([n in self.active for n in neighbors]) - is_active
        if (is_active and num_active in (2, 3)) or (not is_active and num_active == 3):
            self.next_active.add(coords)
        # Add all neighbors to a set to be checked
        if is_active:
            to_check.update(neighbors)
    
    def run_cycles(self, n):
        for _ in range(n):
            self.advance_cycle()
                

if __name__ == "__main__":
    input = load_input()
    game = Game(input, dimension=3)
    game.run_cycles(6)

    game = Game(input, dimension=4)
    game.run_cycles(6)

