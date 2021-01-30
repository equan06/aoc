def load_input():
    with open("input_day9.txt") as f:
        return [int(x) for x in f.read().splitlines()]


"""
A very non-pythonic solution that technically might fail, since 
the two_sum algorithm I implemented is not robust to duplicates
"""
def day9_sol1(input):
    first = 0
    i = 25
    curr = input[i]
    past_25 = set(input[0:25])
    while two_sum(curr, past_25):
        past_25.remove(input[first])
        first += 1
        past_25.add(curr)
        i += 1
        curr = input[i]
    return input[i]

"""
Perform an iterative algorithm to find the first/last indices of the contiguous range, 
then take the min/max.
"""
def day9_sol2(input):
    target_sum = day9_sol1(input)
    first = 0
    last = 0
    curr_sum = input[first]
    while curr_sum != target_sum:
        if curr_sum < target_sum:
            last += 1
            curr_sum += input[last]
        else:
            curr_sum -= input[first]
            first += 1
    return min(input[first:last+1]) + max(input[first:last+1])




"""
Note: this misses the case where the set contains the target / 2, but since we're passing in a set
instead of an array, we can't actually check for duplicates here
"""
def two_sum(target, past_25):
    for x in past_25:
        if target - x in past_25:
            return True
    return False


input = load_input()

print(day9_sol1(input))
print(day9_sol2(input))

