import numpy as np

def load_input():
    with open("input_day10.txt") as f:
        return [int(x) for x in f.read().splitlines()]


def solve_pt1(input):
    input.sort()
    diffs = np.diff(input) 
    n1 = sum([d == 1 for d in diffs]) # num 1s
    return n1 * (len(diffs) - n1 + 1) # num 1s * num 3s

def solve_pt2(input):
    input.sort()
    target = max(input)
    num_ways = dict()
    input_map = set(input)
    for i in input[::-1]:
        for j in input:
            find_num_ways(num_ways, input_map, i, j)
    return num_ways[(0, target)]

"""
Find the number of ways to get from start to end using DP.
Solving (i, j) requires (i + 1, j) so i should be decremented.
Note that the order of j doesn't matter (whether looped first or backwards)
"""
def find_num_ways(num_ways, input_map, start, end):
    if (start, end) in num_ways:
        return num_ways[(start, end)]
    n = 0
    if start >= end:
        n = 0
    elif end - start == 1: # diff 1
        n = 1
    elif end - start <= 3: # diff 2 or 3
        # Jump from start to start + i, and then count num ways from start + i to end
        for i in (1, 2):
            if start + i in input_map:
                n += num_ways[(start + i, end)]
    else:
        for i in (1, 2, 3):
            if start + i in input_map:
                n += num_ways[(start + i, end)]
    num_ways[(start, end)] = n
    return n

if __name__ == "__main__":
    input = load_input()
    input.append(0)
    print(solve_pt1(input))
    print(solve_pt2(input))



