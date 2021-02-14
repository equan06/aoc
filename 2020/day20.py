import re
from itertools import product, combinations
import math

products = list(product(range(0,4), range(0,4), [0,1]))

class Tile:
    def __init__(self, num, grid):
        self.num = num
        self.grid = grid
        self.init_sides()
        self.deg = 0
        self.neighbors = dict()

    def __str__(self):
        return f"\n{str(self.num)}:\n" + str.join("\n", self.grid)

    def init_sides(self):
        self.top = self.grid[0]
        self.bot = self.grid[-1]
        self.lft = str.join("", [g[0] for g in self.grid])
        self.rgt = str.join("", [g[-1] for g in self.grid]) 

    def __getitem__(self, key):
        if key == 0:
            return self.rgt
        elif key == 1:
            return self.top
        elif key == 2:
            return self.lft
        elif key == 3:
            return self.bot
        else:
            return None

    def add(self, tile, i):
        "Save the adjacent tile at location i."
        self.deg += 1
        self.neighbors[i] = tile 
    
    def rot90(self):
        "Assume grid is a list of string rows. Rotate 90 deg ccw."
        ngrid = []
        for c in range(len(self.grid))[::-1]:
            nrow = ""
            for row in self.grid:
                nrow += row[c]
            ngrid.append(nrow)
        self.grid = ngrid
        self.init_sides()
        self.neighbors = {(k + 1) % 4: v for k, v in self.neighbors.items()} # update neighbor locations
        return self

    def flip(self):
        "Flip the grid horizontally."
        ngrid = []
        for r in self.grid:
            ngrid.append(r[::-1])
        self.grid = ngrid
        self.init_sides()
        ndict = dict()
        for k, v in self.neighbors.items(): # update neighbor locations
            if k == 0:
                ndict[2] = v
            elif k == 2:
                ndict[0] = v
            else:
                ndict[k] = v
        self.neighbors = ndict 
        return self

    def trim_grid(self):
        "Remove the borders of the grid."
        ngrid = []
        for line in self.grid:
            ngrid.append(line[1:-1])
        return ngrid[1:-1]

def load_input():
    with open("input_day20.txt") as f:
        res = dict()
        for box in f.read().split("\n\n"):
            lines = box.split("\n")
            key = int(re.search(r"\d+", lines[0]).group(0))
            res[key] = Tile(key, lines[1:])
        return res

def compare(a, b, compared):
    "Check the sides (including reversed) of two Tiles, and connect them if they share a side."
    if a.num == b.num or (a.num, b.num) in compared:
         return
    found = False
    for i, j, sgn in products: 
        if sgn and a[i] == b[j][::-1]:
            found = True
            break
        elif not sgn and a[i] == b[j]:
            found = True
            break
    if found:
        a.add(b, i)
        b.add(a, j)
        compared.add((a.num, b.num))
        compared.add((b.num, a.num))

def rotations(tile):
    "Generator of all possible tile configurations."
    for _ in range(2):
        for _ in range(4):
            yield tile
            tile.rot90()
        tile.flip()

def load_monster():
    "Load the monster's coords (relative to its window) and the size of the monster."
    res = set()
    with open("day20_monster.txt") as f:
        m = [x for x in f.read().splitlines()]
        for idr, row in enumerate(m):
            for idc, token in enumerate(row):
                if token == "#":
                    res.add((idr, idc))
    return res, len(m), len(m[0])

def compare_window(window, m):
    "Assume window has the same dimension as the monster. Return 1 if the monster is found in the current window."
    for r, c in m:
        if window[r][c] != "#":
            return 0
    return 1

def day20(input):
    "This turned into spaghetti real quick..."
    ### DAY 1 ###
    tiles = input # dict of tiles
    compared = set()
    # Find all connections between pairs of tiles
    for a, b in combinations(tiles.values(), 2):
        compare(a, b, compared)
    print(math.prod(v.num for v in tiles.values() if v.deg == 2)) 

    ### DAY 2 ###
    mapgrid = []
    curr_row = []
    next_row = []
    corners = [v for v in tiles.values() if v.deg == 2]

    # find topleft corner (assumes one exists in the correct orientation, but could easily just take the first and rotate/flip...)
    for c in corners:
        if set(c.neighbors.keys()) == {0, 3}:
            next_row.append(c)
            break

    # iterate row by row, and save tiles in their correct orientation
    row = 0
    traversed = set()
    while len(next_row) > 0:
        mapgrid.append([])
        curr_row.append(next_row.pop(0))
        while len(curr_row) > 0:
            curr = curr_row.pop(0) # assume curr is oriented correctly
            traversed.add(curr)
            mapgrid[row].append(curr.trim_grid())

            # find the leftmost tile of the next row and orient it 
            found = False
            if len(next_row) == 0:
                for tile in curr.neighbors.values():
                    if tile in traversed: 
                        continue
                    for r in rotations(tile): 
                        if curr[3] == r[1]:
                            next_row.append(tile)
                            found = True
                            break
                    if found:
                        break
            
            # find the tile to the right and orient it
            found = False
            for tile in curr.neighbors.values():
                if tile in traversed: 
                    continue
                for r in rotations(tile):
                    if curr[0] == r[2]:
                        curr_row.append(tile)
                        found = True
                        break
                if found:
                    break
        row += 1

    # parse mapgrid into a Tile-readable format
    n = len(mapgrid[0][0]) # size of a tile's grid 
    temp = ["" for _ in range(n * len(mapgrid))] # instantiate the rows of the entire map
    r = 0
    for row in mapgrid:
        for icol, tgrid in enumerate(row): 
            for irow, line in enumerate(tgrid): 
                temp[r+irow] += line
        r += n
    maptile = Tile(-1, temp)

    m, rdim, cdim = load_monster()
    num_m = 0   
    for tile in rotations(maptile):
        if num_m > 0:
            break
        rpos = 0 
        while rpos + rdim < len(tile.grid):
            cpos = 0
            while cpos + cdim < len(tile.grid[0]):
                window = [line[cpos:cpos + cdim] for line in tile.grid[rpos:rpos + rdim]]
                num_m += compare_window(window, m)
                cpos += 1
            rpos += 1
    
    return sum(1 if token == "#" else 0 for line in maptile.grid for token in line) - num_m * len(m)
	


if __name__ == "__main__":
    input = load_input()    
    print(day20(input))
