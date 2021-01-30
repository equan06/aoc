import numpy as np


def load_data():
    with open("input_day1.txt") as f:
        return [int(x) for x in f.read().splitlines()]

"""
Day 1 - Part 1

O(n) time - stores every element x in a set, and checks whether the complement 2020 - x exists in the set.
If it does, then x + (2020 - x) == 2020, so return the product.

There's a corner case where 2020/2 = 1010 exists - you'd just skip this one.

My initial solution added the complement to a second set, but you can save space by just checking
the original set. For example, if list = [... 500, ... 1520, ...]

    1) check if 2020 - 500 == 1520 exists in the set - it doesn't, so add 500 to the set
    2) check if 2020 - 1520 == 500 exists in the set - it does, so return solution

"""
def day1_sol1(arr, target):
    s1 = set()
    for x in arr:
        val = target - x
        if val in s1 and val != target//2: 
            return x * val
        s1.add(x)
    return -1


"""
Day 1 - Part 2

This is basically a lazy DP solution: if x, y, z are the solutions, then compute 2020 - x and then find the y, z such that y + z = 2020 - x.

O(n^2) time, as you're computing 2SUM(2020-x) for each x. 
"""
def day1_sol2(arr, target):
    for i, element in enumerate(arr):
        val = target - element
        two_sum = day1_sol1(arr[:i] + arr[i+1:], val)
        if two_sum != -1:
            return two_sum * element
    return -1



input = load_data()
print(day1_sol1(input, 2020))   
print(day1_sol2(input, 2020))



