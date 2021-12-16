import sys
from collections import defaultdict, Counter, deque
import heapq

def load_data(file):
    with open(file) as f:
        return [[int(y) for y in x] for x in f.read().splitlines()]

class minpq:
    """Implementing a minheap using heapq, and added a method to update the priority.
    https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes
    """
    def __init__(this):
        this.pq = []
        this.entry_finder = {}
        this.REMOVED = (-1, -1)

    def add(this, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in this.entry_finder:
            this.remove(task)
        entry = [priority, task]
        this.entry_finder[task] = entry
        heapq.heappush(this.pq, entry)

    def remove(this, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = this.entry_finder.pop(task)
        entry[-1] = this.REMOVED
    
    def popfirst(this):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while this.pq:
            priority, task = heapq.heappop(this.pq)
            if task != this.REMOVED:
                del this.entry_finder[task]
            return task
        raise KeyError('popfirst from an empty priority queue')

    def contains(this, task):
        return task in this.entry_finder.keys()

    def __len__(this):
        return len(this.pq)

def day15_sol1(input):
    return sp(input)

def day15_sol2(input):
    return sp(input, 5)

def sp(input, mult=1):
    def gen(coord):
        for dy in [-1, 0, 1]:
            x, y = coord[0] + 0, coord[1] + dy
            if x < 0 or y < 0 or x >= max_x or y >= max_y: continue
            yield (x, y)
        for dx in [-1, 0, 1]:
            x, y = coord[0] + dx, coord[1] + 0
            if x < 0 or y < 0 or x >= max_x or y >= max_y: continue
            yield (x, y)

    def get_val(coord, input):
        """The coord can now exceed the bounds of the input, and the input values 
        are based on the section of the grid it's in.
        """
        # original coordinates in the input
        x_orig, y_orig = coord[0] % len_x, coord[1] % len_y

        # account for the position in the grid
        add_factor = coord[0] // len_x + coord[1] // len_y
        val = input[y_orig][x_orig] + add_factor 
        return (val - 1) % 9 + 1 # account for the wraparound

    len_x, len_y = len(input), len(input[0])
    max_y, max_x = len_x*mult, len_y*mult
    target = (max_x - 1, max_y - 1)

    q = minpq() # track the node with the current min distance
    dist = defaultdict() # track the min distance to a given coord
    for i in range(0, mult):
        for j in range(0, mult):
            for idy in range(len(input)):
                for idx in range(len(input[0])):
                    x, y = idx + len_x * i, idy + len_y * j
                    dist[(x, y)] = float('inf')
                    q.add((x, y), float('inf'))

    dist[(0, 0)] = 0
    q.add((0, 0), 0)

    # Djikstra's implementation
    while len(q) > 0:
        argmin = q.popfirst()
        if argmin == target: break
        for nbr in gen(argmin):
            if q.contains(nbr):
                curr_dist = dist[argmin] + get_val(nbr, input)
                if curr_dist < dist[nbr]:
                    dist[nbr] = curr_dist
                    q.add(nbr, curr_dist)
    return dist[target]

if __name__ == "__main__":
    file = f"{sys.argv[1]}.txt" if len(sys.argv) > 1 else "input_day15.txt"
    print(file)
    input = load_data(file)
    print(day15_sol1(input))
    print(day15_sol2(input))