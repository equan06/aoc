import numpy as np
import re

def load_data():
    with open("input_day3.txt") as f:
        return [int(x) for x in f.read().splitlines()]

# gotta practice some regex...
def load_data_regex():
    with open("input_day2.txt") as f:
        return [(a, int(b)) for a, b in re.findall(r'^(\w+)\s(\d+)$', f.read().strip(), flags=re.MULTILINE)]

def day1_sol1(input):
    return input
    
def day1_sol2(input):
    return

if __name__ == '__main__':
    input = load_data()
    print(day1_sol1(input))
    print(day1_sol2(input))