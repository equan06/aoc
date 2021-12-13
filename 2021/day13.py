import re
from collections import defaultdict, deque


test = False
def load_data():
    file = "test.txt" if test else "input_day13.txt"
    with open(file) as f:
        dots, folds = list(), list()
        dots_str, folds_str =  f.read().split("\n\n")
        for d in dots_str.splitlines():
            dots.append(list(map(int, d.split(","))))
        for f in folds_str.splitlines():
            grp = re.search(r'([yx])=(\d+)', f)
            # print(grp.group(0)) # group(0) returns the entire match as a string
            folds.append((grp.group(1), int(grp.group(2))))
        return dots, folds

# straightforward solution, only complexity is making sure the indexing is correct when flipping
def day13_sol1(dots, folds):
    ins = folds[0]
    axis, val = ins
    board = set()
    if axis == 'y':
        for d in dots:
            if d[1] > val:
                x, y = d[0], val - (d[1] - val)
            else:
                x, y = d
            board.add((x, y))
    else:
        for d in dots:
            if d[0] > val:
                x, y = val - (d[0] - val), d[1]
            else:
                x, y = d
            board.add((x, y))
    return len(board)

def day13_sol2(dots, folds):
    board = set((x, y) for x, y in dots)
    for axis, val in folds:
        newboard = set()
        if axis == 'y':
            for d in board:
                if d[1] > val:
                    x, y = d[0], val - (d[1] - val)
                else:
                    x, y = d[0], d[1]
                newboard.add((x, y))
        else:
            for d in board:
                if d[0] > val:
                    x, y = val - (d[0] - val), d[1]
                else:
                    x, y = d[0], d[1]
                newboard.add((x, y))
        board = newboard
    
    out = ""
    for y in range(max(c[1] for c in board) + 1):
        for x in range(max(c[0] for c in board) + 1):
            out += "#" if (x, y) in board else " "
        out += "\n"
    return out
            
        
            

if __name__ == '__main__':
    dots, folds = load_data()
    print(day13_sol1(dots, folds))
    print(day13_sol2(dots, folds))