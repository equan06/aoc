def load_input():
    with open('input_day1.txt') as f:
        return [int(x) for x in f.read().splitlines()]

def solve_1pt1(input):
    return sum(mass_to_fuel(m) for m in input)

def solve_1pt2(input):
    return sum(mass_to_fuel(m, True) for m in input)

def mass_to_fuel(mass, recursive = False):
    init_fuel = mass // 3 - 2
    if init_fuel <= 0:
         return 0
    return init_fuel + mass_to_fuel(init_fuel, True) if recursive else init_fuel

if __name__ == '__main__':
    input = load_input()
    print(solve_1pt1(input))
    print(solve_1pt2(input))

