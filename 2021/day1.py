import numpy as np
from timeit import default_timer as timer

def load_data():
    with open("input_day1.txt") as f:
        return [str(x).split(" ") for x in f.read().splitlines()]

def day1_sol1(input):
    print(input)
    return

def day1_sol2(input):
    return


if __name__ == '__main__':
    input = load_data()
    print(day1_sol1(input))
    print(day1_sol2(input))