import numpy as np

def load_input():
    with open("input_day5.txt") as f:
        return [x for x in f.read().splitlines()]

"""
Sol is pretty simple: the first 7 chars are binary for the row #,
and the last 3 chars are binary for the seat #. 
"""
def day5_sol1(input):
    trans = str.maketrans("FBLR", "0101") # Note: if working with a pandas series, use Pd.series.map 
    return max([calc_id(board_pass, trans) for board_pass in input])

"""
Sort first, then compute the differences of all consecutive elements.
The first index with difference 2 (x-1, x+1) will be at x-1,
assuming that all other elements are consecutive.
"""
def day5_sol2(input):
    trans = str.maketrans("FBLR", "0101")
    ids = np.array([calc_id(board_pass, trans) for board_pass in input])
    ids.sort()
    diffs = np.diff(ids)
    return ids[np.nonzero(diffs == 2)[0][0]] + 1


def calc_id(board_pass, trans):
    return int(board_pass[:7].translate(trans), 2) * 8 + int(board_pass[-3:].translate(trans), 2)
    
input = load_input()
print(day5_sol1(input))
print(day5_sol2(input))