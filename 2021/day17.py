from math import ceil
import re

from collections import defaultdict

def load_data():
    with open("input_day17.txt") as f:
        x0, x1, y0, y1 = list(map(int, re.findall(r'-?\d+', f.read())))
    return (x0, x1, y0, y1)

def solve_day17(input):
    x_start, x_end, y_start, y_end = input

    # x is bounded by simple algebra
    max_y = 0
    init_v = set()
    for v_x in range(ceil((x_start*2+.25)**0.5 - 0.5), x_end + 1):
        # there should be some math to find the upper bound of the y velocity but my brain hurts...
        for v_y in range(y_start, 1000):
            path = simulate(v_x, v_y, input)
            valid_path = False
            for p in path:
                if x_start <= p[0] <= x_end and y_start <= p[1] <= y_end:
                    valid_path = True
            if valid_path:
                init_v.add((v_x, v_y))
                curr_y = max(p[1] for p in path)
                max_y = max(max_y, curr_y)
    print(init_v)
    print(len(init_v))
    return max_y
    

def simulate(v_x, v_y, input):
    "Simulate with velocity (v_x, v_y), return the position at each step on the path until it goes outside the bounds"
    # assume initial 0, 0 is never in the target
    traj = []
    step = 0
    x, y = 0, 0
    while x <= input[1] and y >= input[2]: 
        x += v_x
        y += v_y
        traj.append((x, y))
        v_x = v_x - 1 if v_x > 0 else v_x + 1 if v_x < 0 else 0
        v_y -= 1
        step += 1
    return traj

if __name__ == "__main__":
    input = load_data()
    print(input)
    print(solve_day17(input))