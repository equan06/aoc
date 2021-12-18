import sys
from functools import reduce
from collections import defaultdict, Counter, deque


def load_data(file):
    with open(file) as f:
        return [int(x) for x in f.read().splitlines()]

def day17_sol1(input):
    return 

def day17_sol2(input):
    return 


if __name__ == "__main__":
    file = f"{sys.argv[1]}.txt" if len(sys.argv) > 1 else "input_day17.txt"
    print(file)
    input = load_data(file)
    print(day17_sol1(input))
    print(day17_sol2(input))