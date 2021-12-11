import re
from collections import defaultdict
import copy

def load_data():
    with open("input_day11.txt") as f:
        return [list(map(int, x)) for x in f.read().splitlines()]

def day11_sol1(input):
    input = copy.deepcopy(input)
    score = 0
    for i in range(100):
        flashed = set()
        for idy, y in enumerate(input):
            for idx, x in enumerate(y):
                input[idy][idx] = input[idy][idx] + 1
                if input[idy][idx] > 9 and (idx, idy) not in flashed:
                    flashed.add((idx, idy))
                    flash(idx, idy, input, flashed)
        for (x, y) in flashed:
            input[y][x] = 0
        score += len(flashed)
    return score

def day11_sol2(input):
    input = copy.deepcopy(input)
    i = 0
    while True:
        flashed = set()
        for idy, y in enumerate(input):
            for idx, x in enumerate(y):
                input[idy][idx] = input[idy][idx] + 1
                if input[idy][idx] > 9 and (idx, idy) not in flashed:
                    flashed.add((idx, idy))
                    flash(idx, idy, input, flashed)
        for (x, y) in flashed:
            input[y][x] = 0
        i += 1
        if len(flashed) == 100: return i

def flash(idx, idy, input, flashed):
    for i in range(-1, 2):
        for j in range(-1, 2):
            x, y = idx + i, idy + j
            if x == idx and y == idy: continue
            if x < 0 or y < 0 or x == len(input[0]) or y == len(input): continue
            input[y][x] = input[y][x] + 1
            if (input[y][x] > 9 and (x, y) not in flashed):
                flashed.add((x, y))
                flash(x, y, input, flashed)

if __name__ == '__main__':
    input = load_data()
    print(day11_sol1(input))
    print(day11_sol2(input))