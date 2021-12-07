import numpy as np
from collections import defaultdict
import re


def load_data_regex():
    with open("input_day05.txt") as f:
        return [list(map(int, re.findall(r'\d+', x))) for x in f.read().splitlines() for y in x.split("\r\n")]

def day5_sol1(input):
    points = defaultdict(int)
    for line in input:
        x1, y1, x2, y2 = line
        # case 1: horizontal, go from y1 to y2
        if x1 == x2:
            ysign = -1 if y1 > y2 else 1
            for y in range(y1, y2 + ysign, ysign):
                points[(x1, y)] += 1
        elif y1 == y2:
            xsign = -1 if x1 > x2 else 1
            for x in range(x1, x2 + xsign, xsign):
                points[(x, y1)] += 1

    return sum(count >= 2 for count in points.values())
        
def day5_sol2(input):
    points = defaultdict(int)
    for line in input:
        x1, y1, x2, y2 = line
        if x1 == x2:
            ysign = -1 if y1 > y2 else 1
            for y in range(y1, y2 + ysign, ysign):
                points[(x1, y)] += 1
        elif y1 == y2:
            xsign = -1 if x1 > x2 else 1
            for x in range(x1, x2 + xsign, xsign):
                points[(x, y1)] += 1
        else:
            xsign = -1 if x1 > x2 else 1
            ysign = -1 if y1 > y2 else 1
            x, y = x1, y1
            for x, y in zip(range(x1, x2 + xsign, xsign), range(y1, y2 + ysign, ysign)):
                points[(x, y)] += 1
                    
    return sum(count >= 2 for count in points.values())


if __name__ == '__main__':
    input = load_data_regex()
    print(day5_sol1(input))
    print(day5_sol2(input))
