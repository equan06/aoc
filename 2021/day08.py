import re

def load_data():
    with open("input_day08.txt") as f:
        return [re.findall(r"\w+", x) for x in f.read().splitlines()]


def day8_sol1(input):
    count = 0
    known_length = [2, 4, 3, 7]
    for line in input:
        output = line[-4:]
        for pattern in output:
            if len(pattern) in known_length:
                count += 1
    return count

def day8_sol2(input):
    total_sum = 0
    for line in input:
        patterns, output = line[:10], line[10:]
        patterns_to_digit = solve(patterns)
        total_sum += int("".join([str(patterns_to_digit["".join(sorted(pattern))]) for pattern in output]))
    return total_sum

def solve(patterns):
    """Deterministically solve the patterns, and return a mapping of the pattern (chars sorted) to its digit.
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

    # solve for THREE
    for pattern in patterns:
        if len(pattern) == 5 and len(set(pattern).intersection(set(map[7]))) == 3:
            map[3] = pattern
            break
    
    for pattern in patterns:
        if len(pattern) == 6 and len(set(pattern).intersection(set(map[1]))) == 1:
            map[6] = pattern
            break

    for pattern in patterns:
        if len(pattern) == 6 and len(set(pattern).intersection(set(map[4]))) == 4:
            map[9] = pattern

    for pattern in patterns:
        if (len(pattern) == 5) and len(set(pattern).intersection(set(map[6]))) == 5:
            map[5] = pattern
            break

    for pattern in patterns:
        if len(pattern) == 6 and pattern not in map.values():
            map[0] = pattern
            break

    for pattern in patterns:
        if pattern not in map.values():
            map[2] = pattern
            break
    
    return {"".join(sorted(pattern)): digit for digit, pattern in map.items()}

if __name__ == '__main__':
    input = load_data()
    print(day8_sol1(input))
    print(day8_sol2(input))