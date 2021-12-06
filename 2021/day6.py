from functools import lru_cache
import timeit

# days between when a new fish spawns and births
NEW_INTERVAL = 8

# days between when an old fish spawns and births
REPEAT_INTERVAL = 6

def load_data():
    with open("input_day6.txt") as f:
        line = f.read().splitlines()[0]
        return list(map(int, line.split(",")))

# the naive solution
def day6_sol1(input, days):
    input = input[:]
    for day in range(days):
        new_fish = []
        input = [f - 1 for f in input]
        for idf, f in enumerate(input):
            if f == -1:
                new_fish.append(NEW_INTERVAL)
                input[idf] = REPEAT_INTERVAL
        input.extend(new_fish)
    return len(input,)
    
def day6_sol2(input, days):
    return sum(f(fish, days) for fish in input)


@lru_cache(maxsize=None)
def f(k, d):
    """Breaking out the DP for this one!
    f(k, d) returns the number of fish on day d starting with k as the initial internal timer.
    """
    if d == 0:
        return 1
    else:
        # birth a new fish, and continue counting the old fish
        if k == 0:
            return f(REPEAT_INTERVAL, d - 1) + f(NEW_INTERVAL, d - 1)
        else:
            return f(k - 1, d - 1)
    
if __name__ == '__main__':
    input = load_data()
    print(day6_sol1(input, 18))
    print(day6_sol2(input, 256))