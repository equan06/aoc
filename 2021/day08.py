import re

def load_data():
    with open("input_day08.txt") as f:
        return [re.findall(r"\w+", x) for x in f.read().splitlines()]

def day8_sol1(input):
    count = 0
    known_length = [2, 4, 3, 7]
    for line in input:
        output = line[-4:]
        for p in output:
            if len(p) in known_length:
                count += 1
    return count

def day8_sol2(input):
    total_sum = 0
    for line in input:
        patterns, output = line[:10], line[10:]
        patterns_to_digit = solve(patterns)
        total_sum += int("".join([str(patterns_to_digit["".join(sorted(p))]) for p in output]))
    return total_sum

def solve(patterns):
    """Deterministically solve the patterns, and return a mapping of the p (chars sorted) to its digit.
    """
    map = dict()
    for p in patterns:
        if len(p) == 2:
            map[1] = p
        elif len(p) == 4:
            map[4] = p
        elif len(p) == 3:
            map[7] = p
        elif len(p) == 7:
            map[8] = p

    map[3] = next(p for p in patterns if len(p) == 5 and len(set(p) & set(map[7])) == 3)
    
    map[6] = next(p for p in patterns if len(p) == 6 and len(set(p) & set(map[1])) == 1)

    map[9] = next(p for p in patterns if len(p) == 6 and len(set(p) & set(map[4])) == 4)

    map[5] = next(p for p in patterns if len(p) == 5 and len(set(p) & set(map[6])) == 5)

    map[0] = next(p for p in patterns if len(p) == 6 and p not in map.values())

    map[2] = next(p for p in patterns if p not in map.values())
    
    return {"".join(sorted(p)): digit for digit, p in map.items()}

from collections import defaultdict

def brute_force():
    # TODO
    return

if __name__ == '__main__':
    input = load_data()
    print(day8_sol1(input))
    print(day8_sol2(input))
    print(p(input))
