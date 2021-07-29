
def load_input():
    with open('input_day2.txt') as f:
        return [int(x) for x in f.read().split(',')]

def solve_2pt1(input, n = 12, v = 2):
    index = 0
    input[1], input[2] = n, v
    while index < len(input) and parse(input, index):
        index += 4
    return input[0]
    
def solve_2pt2(input):
    for i in range(100):
        for j in range(100):
            if solve_2pt1([x for x in input], i, j) == 19690720:
                return i * 100 + j
    return -1

def parse(program, index):
    """
    Parse and modify the program using the opcode at the given index.
    The opcode can be 1 (add), 2 (mult), or 99 (halt).
    The return value denotes whether the program has completed successfully (halted),
    as certain inputs may cause it to fail.
    """    
    opcode = program[index]
    if opcode == 99:
        return False
    try:
        a, b, c = program[index + 1: index + 4] 
        if opcode == 1:
            program[c] = program[a] + program[b]
        elif opcode == 2:
            program[c] = program[a] * program[b]
        return True
    except:
        return False

if __name__ == '__main__':
    input = load_input()
    print(solve_2pt1(input))
    input = load_input()
    print(solve_2pt2(input))
