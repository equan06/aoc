import numpy as np
from timeit import default_timer as timer

def load_data():
    with open("input_day01.txt") as f:
        return [int(x) for x in f.read().splitlines()]

def day1_sol1(input):
    return sum(1 if x > 0 else 0 for x in np.diff(input))

def day1_sol2(input):
    return sum(i < j for i, j in zip(input[:-3], input[3:]))

def day1_sol3(input):
    acc = 0
    for i in range(len(input)-2):
        acc += input[i] < input[i + 2]     
    return acc

if __name__ == '__main__':
    input = load_data()
    print(day1_sol1(input))
    print(day1_sol2(input)) 