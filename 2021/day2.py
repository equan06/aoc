import numpy as np
import re

def load_data():
    with open("input_day2.txt") as f:
        return [str(x).split(" ") for x in f.read().splitlines()]

# gotta practice some regex...
def load_data_regex():
    with open("input_day2.txt") as f:
        return [(a, int(b)) for a, b in re.findall(r'^(\w+)\s(\d+)$', f.read().strip(), flags=re.MULTILINE)]

def day1_sol1(input):
    depth, horz = 0, 0
    for ins, val in input:
        if ins == "forward":
            horz += int(val)
        elif ins == "up":
            depth -= int(val)
        else:
            depth += int(val)
    return depth * horz

def day1_sol2(input):
    aim, depth, horz = 0, 0, 0
    for ins, val in input:
        if ins == "forward":
            depth += int(val) * aim
            horz += int(val)
        elif ins == "up":
            aim -= int(val)
        else:
            aim += int(val)
    return depth * horz

if __name__ == '__main__':
    input = load_data()
    print(day1_sol1(input))
    print(day1_sol2(input))
    print(load_data_regex())