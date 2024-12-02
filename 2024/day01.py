import re
import itertools
from collections import Counter

def load_input():
    with open("input01.txt") as f:
        flat_list = [int(pair) for line in f.read().splitlines() for pair in re.findall("\d+", line)]

        left, right = [], []
        for idx, x in enumerate(flat_list):
            if idx % 2 == 0:
                left.append(x)
            else:
                right.append(x)
        return [left, right]
        

def sol_p1(left, right):
    left.sort()
    right.sort()
    return sum(abs(l - r) for l, r in zip(left, right))

def sol_p2(left, right):
    right_count = Counter(right)
    return sum(l * right_count.get(l, 0) for l in left)

if __name__ == "__main__":
    input = load_input()
    result_p1 = sol_p1(input[0], input[1])
    print(result_p1)

    result_p2 = sol_p2(input[0], input[1])
    print(result_p2)