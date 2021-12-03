import numpy as np
import re

def load_data():
    with open("input_day3.txt") as f:
        return [list(map(int, x)) for x in f.read().splitlines()]

# gotta practice some regex...
def load_data_regex():
    with open("input_day2.txt") as f:
        return [(a, int(b)) for a, b in re.findall(r'^(\w+)\s(\d+)$', f.read().strip(), flags=re.MULTILINE)]

def day3_sol1(input):
    n = len(input)
    maj = get_maj_np(input)
    min = get_maj_np(input, False)
    gamma = int("".join(["1" if x else "0" for x in maj]), 2)
    epsilon = int("".join(["1" if x else "0" for x in min]), 2)
    print(gamma)
    print(epsilon)
    return gamma * epsilon
 
def day3_sol2(input):
    input2 = list(input)
    idx = 0
    while len(input) > 1:
        thelist = get_maj_np(input) # reuse part 1 function to get majority
        pos = thelist[idx] # use the curr index to find the most common digit
        # filter the input list, keeping numbers that match the most common digit at the current pos.
        # also, tiebreak using 1
        input = list(filter(lambda z: z[idx] == pos if (pos == 1 or pos == 0) else z[idx] == 1, input))
        idx += 1

    gamma = int("".join([str(i) for i in input[0]]), 2)

    idx = 0
    while len(input2) > 1:
        thelist = get_maj_np(input2, False)
        pos = thelist[idx]
        input2 = list(filter(lambda z: z[idx] == pos if (pos == 1 or pos == 0) else z[idx] == 0, input2))
        idx += 1

    epsilon = int("".join([str(i) for i in input2[0]]), 2)
    print(epsilon)
    print(gamma)
    return gamma * epsilon

# 0 brain solution
def get_maj(input, sign = True):
    n = len(input)
    bits = []
    for c in range(len(input[0])):
        bits.append(0)
        for r in range(len(input)):
            bits[c] += int(input[r][c])
    if sign:
        return [1 if x >= n//2+1 else -1 if x == n/2 else 0 for x in np.array(bits)]
    else:
        return [0 if x >= n//2+1 else -1 if x == n/2 else 1 for x in np.array(bits)]

# np column sum. at each index, 1/0 indicates majority/minority digit, -1 indicates tie
def get_maj_np(input, sign = True):
    n = len(input)
    bits = np.sum(input, axis=0)
    if sign:
        return [1 if b >= n//2+1 else -1 if b == n/2 else 0 for b in bits]
    else:
        return [0 if b >= n//2+1 else -1 if b == n/2 else 1 for b in bits]


if __name__ == '__main__':
    input = load_data()
    print(day3_sol1(input))
    print(day3_sol2(input))