def load_input():
    with open("input_day15.txt") as f:
        return [int(x) for x in f.read().split(',')]

"""
Simple and ugly brute force.
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
Version 2.
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

if __name__ == "__main__":
    print(day15_v2(input, 2020))
    print(day15_v2(input, 30000000))