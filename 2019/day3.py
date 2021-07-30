import numpy as np

directions = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

def load_input():
    with open('input_day3.txt') as f:
        return [[ins for ins in wire.split(',')] for wire in f.read().split('\n')]

def solve_3(input):
    a, b = input
    a_wires, b_wires = parse(a), parse(b)
    pt_intersections = set(a_wires.keys()).intersection(set(b_wires.keys())) 

    # pt1: manhattan distance
    min_manh= min(sum(x) for x in pt_intersections)
    # pt2: along-path-distance from origin
    min_delay = min(a_wires[pt] + b_wires[pt] for pt in pt_intersections)

    return min_manh, min_delay
    
def parse(wire):
    """Parse a wire into a dict where the keys are tuple coordinates (representing the wire) and the values are the distance to the coordinate."""
    points = {}
    pos = (0, 0)
    steps = 0
    for ins in wire:
        direction, mag = directions[ins[0]], int(ins[1:])
        for _ in range(mag):
            pos = tuple(sum(p) for p in zip(pos, direction)) 
            steps += 1
            if pos not in points:
                points[pos] = steps # if the wire intersects itself, record the first time only

    return points 

if __name__ == '__main__':
    input = load_input()
    print(solve_3(input))