import re
from collections import defaultdict, deque

test = False
def load_data():
    with open("input_day12.txt") as f:
        adj = defaultdict(set)
        for k, v in [x.split("-") for x in f.read().splitlines()]:
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
    if curr == "end": return 1
    elif curr.islower() and curr not in terminal_nodes:
        if is_dupe and curr in visited: return 0
        elif curr in visited: is_dupe = True
    
    visited.add(curr)
    return sum(dfs2(i, input, set(visited), is_dupe) for i in input[curr])

# Trying this in an iterative style.
# Note: if you implement this using a queue (BFS instead of DFS) then it's much slower than using a stack.
# The reason is because solutions (paths from start to end) can be fairly deep, which means that a queue approach
# will lead to a large queue and overhead (on this input, max length of 500k whereas a stack only goes up to length 37).
# Note that either solution will still visit the same number of vertices in the graph.
def day12_sol2_iter(input):
    paths = 0
    queue = deque()
    queue.append(("start", set(), False))
    while queue:
        curr, curr_path, is_dupe = queue.popleft()
        if curr == "end":
            paths += 1
            continue
        elif curr.islower():
            if is_dupe and curr in curr_path: continue
            elif curr in curr_path: is_dupe = True
        curr_path.add(curr)
        for i in input[curr]:
            queue.appendleft((i, set(curr_path), is_dupe)) # append is much slower, since this turns the DFS into a BFS.
    return paths


if __name__ == '__main__':
    input = load_data()
    print(day12_sol1(input))
    print(day12_sol2(input))
    print(day12_sol2_iter(input))