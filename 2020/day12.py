import numpy as np

def load_input():
    with open("input_day12.txt") as f:
        return [x for x in f.read().splitlines()]

directions = {
    "N": lambda v: [0, v],
    "S": lambda v: [0, -v],
    "E": lambda v: [v, 0],
    "W": lambda v: [-v, 0]
}

degrees = {
    0: "E",
    90: "N",
    180: "W",
    270: "S"
}

# this would be easier to just convert degrees to radians and pass to np.cos/sin 
rotate = {
    0: np.array([[1,0], [0,1]]),
    90: np.array([[0, -1], [1, 0]]),
    180: np.array([[-1, 0], [0, -1]]),
    270: np.array([[0, 1], [-1, 0]])
}

def day12_pt1(input):
    curr_dir = 0
    coords = np.array([0, 0])
    for ins in input:
        act, val = str(ins[0]), int(ins[1:])
        if act == "L":
            curr_dir = (curr_dir + val) % 360
        elif act == "R":
            curr_dir = (curr_dir - val) % 360
        elif act == "F":
            coords += directions[degrees[curr_dir]](val)
        else:
            coords += directions[act](val)
    print(coords)
    return abs(coords[0]) + abs(coords[1])


def day12_pt2(input):
    coords = np.array([0, 0])
    waypoint = np.array([10, 1])
    for ins in input:
        act, val = str(ins[0]), int(ins[1:])
        if act == "L":
            waypoint = np.matmul(rotate[val], waypoint)
        elif act == "R":
            waypoint = np.matmul(rotate[360 - val], waypoint)
        elif act == "F":
            coords += waypoint * val
        else:
            waypoint += directions[act](val)
    print(waypoint, coords)
    return abs(coords[0]) + abs(coords[1])


if __name__ == "__main__":
    input = load_input()
    print(day12_pt1(input))
    print(day12_pt2(input))
