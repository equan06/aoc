import numpy as np
from math import prod
import operator
from functools import reduce

def load_input():
    with open("input_day3.txt") as f:
        return [x for x in f.read().splitlines()]

"""
Sol is pretty simple: iterate through the rows of the forest by multiples of 'down', and then
use modulus to take care of moving to the next forest
"""
def move_down(input, right = 3, down = 1):
    count, i = 0, 0
    for index, row in enumerate(input):
        if index % down != 0: continue
        if row[i] == "#": 
            count += 1
        i = (i + right) % len(row)
    return count

def day3_sol1(input):
    return move_down(input) 

"""
Note: originally I used np.prod, but np uses 64 bit ints - aka it overflows
So to get the product of all elements of an array:
1) prod(arr)
2) reduce(operator.mul, arr, 1)
"""
def day3_sol2(input):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return prod([move_down(input, right, down) for (right, down) in slopes])
  
input = load_input()
print(day3_sol1(input))
print(day3_sol2(input))


