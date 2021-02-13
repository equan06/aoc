import re
import numpy as np

def load_input():
    with open("input_day19.txt") as f:
        return f.read()


def parse(input):
    rules = {k: v for k, v in re.findall(r"^(\d+):\s(.*)$", input, flags=re.MULTILINE)}
    messages = [line for line in re.findall(r"^[ab]+$", input, flags=re.MULTILINE)]
    print(rules)
    return rules, messages


class Verifier:
    """This is a different approach from before, where we essentially check a message by applying rules to that message. 
    Code is mainly from george hotz's solution
    """
    def __init__(self, input):
        self.rules, self.messages = parse(input)

    def solve1(self):
        return sum(self.verify(m, "0") == len(m) for m in self.messages)

    def solve2(self):
        self.rules["8"] = "42 | 42 8"
        self.rules["11"] = "42 31 | 42 11 31"
        return [self.verify2(m, "0") for m in self.messages]

    def verify(self, message, r):
        "Check message against the rule r. 3 possible rules: end rule, OR rule, AND rule."
        rules = self.rules[r]
        curr = 0
        if rules[0].startswith('"'): 
            return 1 if message[0] == rules[1] else -1
        for main in rules.split(" | "): # split rules by OR 
            curr = 0 # num of correct matches of the current message
            for sub in main.split(" "): # split rules by AND
                res = self.verify(message[curr:], sub)
                if res == -1:
                    break
                curr += res
            if res != -1:
                return curr  
        return curr if curr == len(message) else -1

    def verify2(self, message, r):
        """
        Returns a list, where each element is the number of consecutive matches starting from the left.
        Basically, modified to check multiple paths at a branch instead of only the current (correct) path. For 8/11: if you go left then you need to check all subsequent rules after matching the left side (finite),
        but then you also need to check right instead of returning early (in case left succeeded, but then failed a future match).
        """
        if len(message) == 0:
            return []
        rules = self.rules[r]
        if rules[0].startswith('"'): 
            return [1] if message[0] == rules[1] else []
        ret = [] 
        for main in rules.split(" | "): # split rules by OR 
            curr = [0] # track the current number of matches
            for sub in main.split(" "): # split rules by AND
                newcurr = []
                for c in curr:
                    results = self.verify2(message[c:], sub)
                    newcurr += [c + res for res in results]
                curr = newcurr
            ret += curr
        return ret
            
                

        

input = load_input()
v = Verifier(input)
print(v.solve1())
print(v.solve2())