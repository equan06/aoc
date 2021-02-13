import re
from itertools import product
import numpy as np

def load_input():
    with open("input_day19.txt") as f:
        return [x for x in f.read().splitlines()]


def day19_pt1(input):
    """Brute force approach - generate all valid messages, then check all messages against the rules."""
    rules, messages = parse(input)
    t = Tree(rules)
    res = set(t.build_rules(0))
    return sum(1 for m in messages if m in res)

def day19_pt2(input):
    "This uses some observations about rule 0 - see check2"
    rules, messages = parse(input)
    t = Tree(rules)
    # Build rule 0 manually
    r42 = set(t.build_rules(42))
    r31 = set(t.build_rules(31)) 
    return sum(t.check2(m, r42, r31) for m in messages)
        
def parse(input):
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
        "Return a list of all valid strings according to the rule r. Uses some pretty ugly calls to product..."
        if r in self.valid:
            return self.valid[r]
        root = self.rules[r]
        if len(root) == 1: 
            # parse a leaf 
            if type(root[0][0]) == str: # [["a"]]
                self.valid[r] = root[0]
                return root[0]
            else: # [[1, 2, 3]]
            # parse the AND
                sequence = [self.build_rules(c) for c in root[0]]
                # compute cart. product of the sequence, and save to valid
                v = ["".join(i) for i in product(*sequence)]
                self.valid[r] = v 
                return v
        elif len(root) == 2: # [[1,2], [3,4]]
            # process the OR
            left = [self.build_rules(c) for c in root[0]]
            right = [self.build_rules(c) for c in root[1]]
            v = ["".join(i) for i in product(*left)] + ["".join(i) for i in product(*right)]
            self.valid[r] = v
            return v
        else:
            raise Error

    def check2(self, msg, r42, r31):
        """Part 2: check msg against rule 0 manually, since 0: 8 11. The message must have form
        42^i + 42^j + 31^j where i > j. Also note that all messages of rule 42 and 31 have length 8, so all you have to do is 
        check multiples of 8 where # consec sets of 42 > # consec sets of 31!
        """
        if len(msg) % 8 != 0 or len(msg) < 8:
            return 0
        curr, consec42, consec31 = 0, 0, 0
        mode = 42
        while curr < len(msg):
            sub = msg[curr:curr+8]  
            # intersection btwn 42 and 31 is empty
            if sub in r42 and mode == 42: # check consec 42s
                consec42 += 1
                prev = 42
            elif sub in r31: # switch to checking consec 31s
                if mode == 42:
                    mode = 31 
                consec31 += 1
            else:
                return 0
            curr += 8   
        return 1 if consec31 > 0 and consec42 > consec31 else 0


input = load_input()
print(day19_pt1(input))
print(day19_pt2(input))