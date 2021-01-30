import re

def load_input():
    with open("input_day8.txt") as f:
        return [x for x in f.read().splitlines()]


"""
Straightforward instruction loop
"""
def day8_sol1(input):
    visited = set()
    i = 0
    acc = 0
    while (i < len(input) and i >= 0):
        if i in visited:
            return acc
        visited.add(i)
        instruction = input[i][:3]
        value = re.search(r'[+-]\d+', input[i]).group(0)
        value = int(value[1:]) if value[0] == "+" else int(value)
        if instruction == "nop":
            i += 1
        elif instruction == "acc":
            acc += value
            i += 1
        else:
            i += value
    return acc

"""
Brute-force by checking each nop/jmp to see if switching it terminates the loop.
"""
def day8_sol2(input):
    is_inf = False
    switch_index = 0
    while (not is_inf):
        is_inf, acc = run_instructions(switch_index)
        switch_index += 1
    return acc
        
"""
Run the current instructions, but invert the ith nop/jump instruction (at invert_i).
Return a tuple (is_inf, acc) 
"""
def run_instructions(invert_i):
    visited = set()
    curr_instruction = 0
    i = 0
    acc = 0
    while (i < len(input) and i >= 0):
        if i in visited:
            return (False, acc)
        visited.add(i)
        instruction = input[i][:3]
        value = re.search(r'[+-]\d+', input[i]).group(0)
        value = int(value[1:]) if value[0] == "+" else int(value)
        if instruction == "nop":
            i += value if curr_instruction == invert_i else 1
            curr_instruction += 1
        elif instruction == "acc":
            acc += value
            i += 1
        else:
            i += 1 if curr_instruction == invert_i else value
            curr_instruction += 1
    return (True, acc)

input = load_input()
print(day8_sol1(input))
print(day8_sol2(input))
