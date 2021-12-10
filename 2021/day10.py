import re
from collections import defaultdict

def load_data():
    with open("input_day10.txt") as f:
        return [x for x in f.read().splitlines()]

pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

points2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

def day10_sol1(input):
    """Use a stack to track the most recent "start" bracket. 
    When an "end" bracket is encountered, check against the last added "start" bracket.
    """
    illegal = []
    for line in input:
        starts = []
        for c in line:
            if c in pairs.keys():
                starts.append(c)
            else:
                if c != pairs[starts[-1]]:
                    illegal.append(c)
                    break
                starts.pop()
    return sum(points[i] for i in illegal)

def day10_sol2(input):
    scores = []
    for line in input:
        starts = []
        corr = False
        for c in line:
            if c in pairs.keys():
                starts.append(c)
            else:
                if c != pairs[starts[-1]]:
                    corr = True
                    break
                starts.pop()
        if not corr and len(starts) > 0:
            score = 0
            for s in reversed(starts):
                score = score * 5 + points2[s]
            scores.append(score)
    scores.sort()
    return scores[len(scores)//2]

if __name__ == '__main__':
    input = load_data()
    print(day10_sol1(input))
    print(day10_sol2(input))