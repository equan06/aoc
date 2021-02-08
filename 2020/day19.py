import re
from itertools import product
import numpy as np

def load_input():
    with open("input_day19.txt") as f:
        return [x for x in f.read().splitlines()]

def day18_pt1(input):
    rules, messages = parse(input)
    t = Tree(rules)
    res = set(t.build_rules(0))
    return sum(1 for m in messages if m in res)
        

def day18_pt2(input):
    rules, messages = parse(input)
    t = Tree(rules)
    t.build_rules(0)
    print(rules[31])
    print(rules[42])
    # anything containing 8 or 11 will now have loops
    # rules[8] = [[42], [42, 8]]
    # rules[11] = [[42, 31], [42, 11, 31]]
    # find all rules not containing 8, 11, and parse the messages - add a is_finite set to Tree
    # take the remaining messages
    #

def parse(input):
    # print(re.findall(r"^(\d+):\s(\d+)\s(\d+)\s\|\s(\d+)\s(\d+)$", input, flags=re.MULTILINE))
    # rules = {int(line[0]): [list(map(int, line[1:3])), list(map(int, line[3:5]))] for line in re.findall(r"^(\d+):\s(\d+)\s(\d+)\s\|\s(\d+)\s(\d+)$", input, flags=re.MULTILINE)}
    # print(re.findall(r"^(\d+):\s(\d+)\s(\d+)\s(?!\|)", input, flags=re.MULTILINE))
    messages = []
    rules = dict()
    rows = (re.findall("[\d\|]+|[\w]+", row) for row in input)
    for r in rows:
        if len(r) == 0:
            continue
        elif len(r) == 1:
            messages.append(r[0])
        elif "|" in r:
            i = r.index("|")
            rules[int(r[0])] = [list(map(int, r[1:i])), list(map(int, r[i+1:]))]
        elif r[1] in "ab":
            rules[int(r[0])] = [r[1]]
        else:
            rules[int(r[0])] = [list(map(int, r[1:]))]
    return rules, messages

class Tree:
    def __init__(self, rules):
        self.rules = rules
        self.valid = dict()
        self.is_finite = set()

    def build_rules(self, r):
        "Return a list of valid strings according to the rule r."
        if r in self.valid:
            return self.valid[r]
        root = self.rules[r]
        if len(root) == 1: 
            # parse a leaf 
            if type(root[0][0]) == str: # [["a"]]
                self.valid[r] = root[0]
                return root[0]
            else: # [[1, 2, 3]]
            # parse the rule sequentially 
                sequence = [self.build_rules(c) for c in root[0]]
                # compute cart. product of the sequence, and save to valid
                v = ["".join(i) for i in product(*sequence)]
                self.valid[r] = v 
                return v
        elif len(root) == 2: # [[1,2], [3,4]]
            # process the or
            left = [self.build_rules(c) for c in root[0]]
            right = [self.build_rules(c) for c in root[1]]
            v = ["".join(i) for i in product(*left)] + ["".join(i) for i in product(*right)]
            self.valid[r] = v
            return v
        else:
            raise Error

    


input = load_input()
# print(day18_pt1(input))
print(day18_pt2(input))