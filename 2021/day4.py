import numpy as np
import re
from functools import reduce

# first attempt - ugly, but it worked...
def load_data():
    with open("input_day4.txt") as f:
        arr = [re.sub(r'\s+', ',', re.sub(r'^\s+', '', y, flags=re.MULTILINE)).split(",") for x in f.read().splitlines() for y in x.split("\r\n") ]
        input = list(map(int, arr[0]))
        print(arr)
        print(input)
        boards = []
        curr = []
        for line in arr[1:]:
            if len(line) == 1:
                if len(curr) > 0:
                    boards.append(curr)
                curr = []
            else:
                curr.append(list(map(int, line)))
        boards.append(curr)
        print(boards)
        return input, boards


# going back and practicing some regex
def load_data_regex():
    with open("input_day4.txt") as f:
        arr = [list(map(int, re.findall(r'\d+', x))) for x in f.read().splitlines() for y in x.split("\r\n")]
        input = arr[0]
        boards = []
        curr = []
        for line in arr[1:]:
            if len(line) == 0:
                if len(curr) > 0:
                    boards.append(curr)
                curr = []
            else:
                curr.append(line)    
        boards.append(curr)
        return input, boards


# check for bingo
def score_board(board, marked):
    n = len(board)
    # check columns
    is_bingo = any(all((r, c) in marked for c in range(n)) for r in range(n))
    if is_bingo:
        return True
    # check rows
    return any(all((r, c) in marked for r in range(n)) for c in range(n))

def day1_sol1(input, boards):
    tracker = [set() for _ in boards]
    n = len(boards[0])
    for num in input:
        for idb, b in enumerate(boards):
            for x in range(n):
                for y in range(n):
                    if b[x][y] == num:
                        tracker[idb].add((x,y))
            # find first bingo and score the unmarked squares
            if score_board(b, tracker[idb]):
                score = sum(b[x][y] for x in range(n) for y in range(n) if (x, y) not in tracker[idb])
                return score * num
    return -1

def day1_sol2(input, boards):
    tracker = [set() for _ in boards]
    n = len(boards[0])
    skip_board = set() # boards to skip once bingo accomplished
    for num in input:
        for idb, b in enumerate(boards):
            if idb in skip_board:
                continue
            for x in range(n):
                for y in range(n):
                    if (b[x][y] == num):
                        tracker[idb].add((x,y))
            if score_board(b, tracker[idb]):
                skip_board.add(idb)
                # when the last bingo is found, score the board
                if len(skip_board) == len(boards):
                    score = sum(b[x][y] for x in range(n) for y in range(n) if (x, y) not in tracker[idb])
                    return score * num
    return -1


if __name__ == '__main__':
    input, boards = load_data_regex()
    print(day1_sol1(input, boards))
    print(day1_sol2(input, boards))