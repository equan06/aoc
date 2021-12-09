import re
from collections import defaultdict

def load_data():
    with open("input_day09.txt") as f:
        return [list(map(int, x)) for x in f.read().splitlines()]

def day9_sol1(input):
    return sum(x + 1 for idy, y in enumerate(input) for idx, x in enumerate(y) if validate(input, idx, idy))

def day9_sol2(input):
    low = [(idx, idy) for idy, y in enumerate(input) for idx, x in enumerate(y) if validate(input, idx, idy)]
    sizes = [dfs(input, point[0], point[1], -1) for point in low]
    sizes.sort()
    a, b, c = sizes[-3:]
    return a * b * c
    
visited = set()
def dfs(input, idx, idy, prev):
    """Starting from a low point, dfs to find the size of the basin connecting to the low point.
    Use visited to track already entered vertices (if visited, it's already part of a basin)
    """
    lenx, leny = len(input[0]), len(input)
    if (idx, idy) in visited:
        return 0
    if idx < 0 or idy < 0 or idx == lenx or idy == leny:
        return 0
    curr  = input[idy][idx]
    if curr <= prev or curr == 9:
        return 0
    visited.add((idx, idy))
    ret = 1
    ret += dfs(input, idx + 1, idy, prev)
    ret += dfs(input, idx - 1, idy, prev)
    ret += dfs(input, idx, idy + 1, prev)
    ret += dfs(input, idx, idy - 1, prev)
    return ret

def validate(input, idx, idy):
    """Check whether the current point is a low point (all adjacent, nondiagonal neighbors are strictly greater than the current)
    """
    a, b, c, d = [True for _ in range(4)]
    lenx, leny = len(input[0]), len(input)
    val = input[idy][idx]
    if idx > 0:
        a= val < input[idy][idx - 1]
    if idx + 1 < lenx:
        b = val < input[idy][idx + 1]
    if idy > 0:
        c = val < input[idy - 1][idx]
    if idy + 1 < leny:
        d = val < input[idy + 1][idx]
    return a and b and c and d

if __name__ == "__main__":
    input = load_data()
    print(day9_sol1(input))
    print(day9_sol2(input))