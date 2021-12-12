import re
from collections import defaultdict, Counter
import copy
test = False
def load_data():
    file = "test.txt" if test else "input_day12.txt"
    with open(file) as f:
        l = [x.split("-") for x in f.read().splitlines()]
        adj = defaultdict(set)
        for k, v in l:
            adj[k].add(v)
            if k != "start" and v != "end":
               adj[v].add(k)
        return adj

terminal_nodes = ("start", "end")

def day12_sol1(input):
    return dfs("start", input, set())

# Return a list of all paths that start from curr and go to end.
def dfs(curr, input, visited):
    if curr == "end": return 1
    elif curr.islower() and curr in visited: return 0
    
    visited.add(curr)
    return sum(dfs(i, input, set(visited)) for i in input[curr])
    
def day12_sol2(input):
    return dfs2("start", input, set(), False)

# Count all paths to "end" starting from curr, and using visited and is_dupe to check the conditions on the lowercase vertices
def dfs2(curr, input, visited, is_dupe):
    if curr == "end":
        return 1
    elif curr.islower() and curr not in terminal_nodes:
        if is_dupe and curr in visited: return 0
        elif curr in visited: is_dupe = True
    
    visited.add(curr)
    return sum(dfs2(i, input, set(visited), is_dupe) for i in input[curr])

if __name__ == '__main__':
    input = load_data()
    print(day12_sol1(input))
    print(day12_sol2(input))