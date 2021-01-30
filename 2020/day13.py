import regex as re
import numpy as np

def load_input():
    with open("input_day13.txt") as f:
        return [x for x in f.read().splitlines()]
"""
Quick note: -t mod b is the distance from earliest <= b
"""
def day13_pt1(input):
    earliest = int(input[0])
    buses = [int(b) for b in re.findall(r'\d+', str(input[1]))]
    min_time = [(-1*earliest) % b for b in buses]
    i = np.argmin(min_time)
    return buses[i] * min_time[i]

"""
Gauss algorithm to solve a modular system
https://shainer.github.io/crypto/math/2017/10/22/chinese-remainder-theorem.html

Basically, we have a modular equation for each bus:
    t = a_i mod n_i where a_i = -bus_idx and n_i = bus_id
and the problem reduces to finding the smallest t that satisfies the above.
"""
def day13_pt2(input):
    remainders, moduli = [], []
    N, x = 1, 0
    for idx, b in enumerate(input[1].split(',')):
        if b != "x":
            # note: idx itself is not the correct remainder
            # eg: if t+1 = 0 mod 13, t = -1 mod 13
            remainders.append(-1*idx)
            moduli.append(int(b))
            N *= int(b)
    for ai, ni in zip(remainders, moduli):
        bi = N // ni
        x += ai*bi*pow(bi, -1, ni)
    return x % N # return the smallest such solution (unique modulo N)
    
input = load_input()
print(day13_pt1(input))
print(day13_pt2(input))