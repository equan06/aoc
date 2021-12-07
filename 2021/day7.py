import numpy as np

def load_data():
    with open("input_day7.txt") as f:
        return list(map(int, f.read().split(",")))

def day7_sol1(input):
    min_fuel, argmin = float('inf'), -1
    for i in range(min(input), max(input)):
        cost = sum(np.abs(np.array(input) - i))
        if cost < min_fuel:
            min_fuel, argmin = cost, i
    return min_fuel
    
def day7_sol2(input):
    min_fuel, argmin = float('inf'), -1
    for i in range(min(input), max(input)):
        # cost function is now 1 + 2 + ... + n = n*(n+1)/2, where n is the distance
        n = np.abs(np.array(input) - i)
        cost = sum(n*(n+1)/2)
        if cost < min_fuel:
            min_fuel, argmin = cost, i
    return min_fuel

def day7_sol1_oneline(input):
    return min(sum(abs(x - i) for x in input) for i in range(min(input), max(input)))

def day7_sol2_oneline(input):
    return min(sum(map(lambda n: n*(n+1)/2, (abs(x - i) for x in input))) for i in range(min(input), max(input)))

if __name__ == '__main__':
    input = load_data()
    print(day7_sol1(input))
    print(day7_sol1_oneline(input))
    print(day7_sol2(input))
    print(day7_sol2_oneline(input))