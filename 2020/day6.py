import numpy as np

def load_input():
    with open("input_day6.txt") as f:
        return [x for x in f.read().split("\n\n")]

"""
Fairly straightforward - compute all distinct letters in each group's string
"""
def day6_sol1(input):
    return sum([len(set(group.replace("\n", ""))) for group in input])


"""
Unlike the above sol, now you have to actually make distinctions between lines of a group.
"""
def day6_sol2(input):
    return sum([calc_group(group.split("\n")) for group in input])


"""
Assumes that group is a list of each person's answers.

Note: *[list] is different from def foo(*args). In this context, it's being used to 
unpack a list and pass the elements of that list as function parameters.
"""
def calc_group(group):
    return len(set.intersection(*[set(person) for person in group]))

input = load_input()
print(day6_sol1(input))
print(day6_sol2(input))
