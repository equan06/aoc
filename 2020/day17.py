import itertools
def load_input():
    with open("input_day17.txt") as f:
        return [x for x in f.read().splitlines()]


# Conventions: first level contains z-slices, each z-slice contains the x-y plane with rows parallel to the x-axis

class SpaceND:
    def __init__(self, n, *args):
        if len(args) != n:
            print("The dimension was not equal to the number of parameters passed in.")
            print(args, n)
            return
        self.dimension = n
        self.initialize_dimension_sizes(args)
        z = args[-1]
        self.z_range = [-(z//2), z - z//2]
        self.z_origin = z//2
        self.z_len = z
        # initial size of the subspaces, for creating new spaces
        self.init_args = args[:-1]
        # base case - if n=3 create a list of planes (this could be refactored into SpaceND, but too much work)
        if n == 3:
            self.z_planes = [Plane(args[0], args[1], z) for z in range(self.z_range[0], self.z_range[1])]
        else:
            self.z_planes = [SpaceND(n-1, *args[:-1]) for z in range(self.z_range[0], self.z_range[1])]

    def initialize_dimension_sizes(self, args):
        self.dimension_sizes = dict()
        for i in range(self.dimension):
            self.dimension_sizes[i + 1] = args[i]

    # todo: check that get/set actually work with a spacend object?
    def __getitem__(self, key):
        new_z = self.z_origin + key[-1]
        if new_z > self.z_len - 1 or new_z < 0:
            return -1
        return self.z_planes[new_z][key[:-1]]

    def __setitem__(self, key, value):
        new_z = self.z_origin + key[-1]
        while new_z > self.z_len - 1 or new_z < 0:
            self.add_z_plane(new_z > self.z_len - 1)
            new_z = self.z_origin + key[-1]
        self.z_planes[new_z][key[:-1]] = value

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.z_len:
            self.n += 1
            return self.z_planes[self.z_len - self.n]
        else:
            raise StopIteration

    def add_z_plane(self, pos = True):
        if pos:
            self.z_planes.append(SpaceND(self.dimension - 1, *self.init_args))
        else:
            self.z_planes.insert(0, SpaceND(self.dimension - 1, *self.init_args))
        self.z_len += 1
        self.z_origin += not pos

    def __str__(self):
         return str.join("\n", [str(z) for z in self.z_planes[::-1]])

    def count_active(self):
        return sum([plane.count_active() for plane in self.z_planes])

    def print(self, z):
        print(str(self.z_planes[self.z_origin + z]))
        
"""Decided to take a detour instead of solving the problem directly. """
class Plane:
    # Initialize an x by y grid around the origin. 
    def __init__(self, x=3, y=3, z=0):
        self.y_rows = [["." for i in range(x)] for j in range(y)]
        self.x_origin = x//2
        self.y_origin = y//2
        self.x_len = x
        self.y_len = y
        self.z = z
        self.dimension_sizes = {1: self.x_len, 2: self.y_len }
 

    # Index so that key is the offset from the origin.
    def __getitem__(self, key):
        new_x = self.x_origin + key[0]
        new_y = self.y_origin + key[1]
        if new_y > self.y_len - 1 or new_y < 0 or new_x > self.x_len - 1 or new_x < 0:
            return -1
        return self.y_rows[new_y][new_x]

    def __setitem__(self, key, value):
        new_x = self.x_origin + key[0] # x is stored as [-1, 0, 1]
        new_y = self.y_origin - key[1] # by convention, the y-index is reversed [1, 0, -1] for printability 
        while new_y > self.y_len - 1 or new_y < 0:
            self.add_y_row(new_y > self.y_len - 1)
            new_y = self.y_origin - key[1]
        while new_x > self.x_len - 1 or new_x < 0:
            self.add_x_row(new_x > self.x_len - 1)
            new_x = self.x_origin + key[0]
        self.y_rows[new_y][new_x] = value
         

    def add_y_row(self, pos = True):
        if pos:
            self.y_rows.insert(0, ["." for _ in range(self.x_len)])
        else:
            self.y_rows.append(["." for _ in range(self.x_len)])

        self.y_len += 1
        self.y_origin += pos

    def add_x_row(self, pos = True):
        [y.append(".") if pos else y.insert(0, ".") for y in self.y_rows]
        self.x_len += 1
        self.x_origin += not pos


    def __str__(self):
        return f"\nz = {self.z}\n" + str.join("\n", [str.join("", y_row)  for y_row in self.y_rows])

    def origin(self):
        return (self.x_origin, self.y_origin)

    def size(self):
        return (self.x_len, self.y_len)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.y_len:
            self.n += 1
            return self.y_rows[self.y_len - self.n]
        else:
            raise StopIteration
    
    def count_active(self):
        return sum([i == "#" for row in self.y_rows for i in row])


class GameND:
    def __init__(self, input, n, *args):

        self.dimension = n
        self.cycle = 0
        self.state = SpaceND(self.dimension, *args)
        self.next_state = SpaceND(self.dimension, *args)
        self.init_args = args
        self.num_active = 0
        self.set_initial_ranges()
        self.set_initial_conditions(input)

    def set_initial_conditions(self, input):
        if not self.ranges:
            self.set_initial_ranges()
        self.num_active = 0
        len_y = len(input)
        len_x = len(input[0])
        print(len_x, len_y)
        lb_y = len_y//2 
        lb_x = len_x//2 
        self.x_range = [-lb_x, len_x - lb_x - 1]
        self.y_range = [-lb_y, len_y - lb_y - 1]
        self.ranges[1] = self.x_range
        self.ranges[2] = self.y_range
        zero_pad = [0 for _ in range(self.dimension - 2)] if self.dimension > 2 else []
        for y in range(0, len_y):
            for x in range(0, len_x):
                next_input = input[y][x]   
                self.num_active += 1 if next_input == "#" else 0
                coord = [x - lb_x, len_y - lb_y - y - 1] + zero_pad
                self.state[coord] = next_input
        print(self.num_active)

    def set_initial_ranges(self):
        self.ranges = dict()
        for i in range(self.dimension):
            self.ranges[i + 1] = [0, 0]

    def advance_cycle(self):
        self.cycle += 1
        print(f"cycle: {self.cycle}")
        self.increment_ranges()

        self.check_cells_ndim()
        self.state = self.next_state
        self.next_state = SpaceND(self.dimension, *self.init_args)

    def increment_ranges(self):
        for rng in self.ranges.values():
            rng[0] -= 1
            rng[1] += 1


    def check_cells_ndim(self):
        for coord in list(itertools.product(*[[i for i in range(rng[0], rng[1] + 1)] for rng in self.ranges.values()])):
            self.check_cell(coord)

    def check_cell(self, curr_coords):
        is_active = self.state[curr_coords] == "#"
        num_neighbors = 0
        coords = [[coord + adj for adj in [-1, 0, 1]] for coord in curr_coords]
        all_neighbors = list(itertools.product(*coords))
        num_neighbors = sum([self.state[neighbor_coords] == "#" for neighbor_coords in all_neighbors])
        num_neighbors -= is_active # if active, then we counted the curr_coords as a neighbor
        if is_active and (num_neighbors == 2 or num_neighbors == 3):
            self.next_state[curr_coords] = "#"
        elif is_active:
            self.num_active -= 1
            self.next_state[curr_coords] = "."
        elif (not is_active and num_neighbors == 3):
            self.next_state[curr_coords] = "#"
            self.num_active += 1
        else:
            self.next_state[curr_coords] = "."


sample_input = [".#.", "..#", "###"]
input = load_input()

game1 = GameND(input, 3, 27, 27, 13)
for i in range(6):
    game1.advance_cycle()
    print(game1.num_active)


game2 = GameND(input, 4, 27, 27, 13, 13)

for i in range(6):
    game2.advance_cycle()
    print(game2.num_active)



