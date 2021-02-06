import timeit

def load_input():
    with open("input_day15.txt") as f:
        return [int(x) for x in f.read().split(',')]

"""
Simple and ugly brute force.
Also note that key in dictionary.keys() is much slower than key in dictionary:
    dictionary.keys() has to create a view object, whereas dictionary already acts as a set
"""
def day15_v1(input, turns = 2020):
    turn = 1
    last = 0
    last_spoken = dict() # keys are spoken numbers, values are the last turn spoken
    while turn <= turns:
        if turn <= len(input):
            last = input[turn - 1]
            last_spoken[last] = (-1, turn)
        else:
            if last in last_spoken.keys() and last_spoken[last][1] <= len(input):
                last = 0
                last_spoken[last] = (last_spoken[last][1], turn)
            elif last in last_spoken.keys() and last_spoken[last] == (-1, turn - 1):
                last = 0
                last_spoken[last] = (last_spoken[last][1], turn)
            else:
                last = turn - 1 - last_spoken[last][0]
                if (last in last_spoken.keys()):
                    last_spoken[last] = (last_spoken[last][1], turn)
                else:
                    last_spoken[last] = (-1, turn)
        turn += 1
    return last

"""
Version 2. Runs roughly twice as fast as version 1, but logic is
still really ugly
"""
def day15_v2(input, turns = 2020):
    turn = 1
    last = 0
    last_spoken = dict()
    is_first = True
    last_zero = 0
    while turn <= turns:
        if turn <= len(input):
            last = input[turn - 1]
            last_spoken[last] = (-1, turn)
            if last == 0:
                last_zero = turn
        else:
            if is_first:
                last = 0
                is_first = False
                diff = turn - last_zero
                last_zero = turn
            else:
                last = diff
                temp = last_spoken.get(last)
                if not temp:
                    is_first = True
                    last_spoken[last] = (-1, turn)
                else:
                    last_spoken[last] = (temp[1], turn)
                    diff = turn - temp[1]
            
        turn += 1
    return last

"""
Implemented Pete Norvig's solution - turns out the branching makes my code much slower
over millions of iterations
"""
def day15_v3(input, turns = 2020):
    last = input[-1]
    # 1st number last spoken on turn 0
    last_spoken = {num: t for t, num in enumerate(input)}
    for t in range(len(input), turns):
        curr = 0 if last not in last_spoken else t - 1 - last_spoken[last]
        last_spoken[last] = t - 1
        last = curr
    return last
        

if __name__ == "__main__":
    input = load_input()
    print(day15_v2(input, 2020))
    t = timeit.Timer(lambda: day15_v2(input, 30000000))
    print(t.timeit(2))
    t = timeit.Timer(lambda: day15_v3(input, 30000000))
    print(t.timeit(2))