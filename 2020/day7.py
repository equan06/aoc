import re

def load_input():
    with open("input_day7.txt") as f:
        return [x for x in f.read().splitlines()]


"""
Input a rule, and add it to the dict of relationships
"""
def parse_rule(rule, relationships):

    bags = re.findall(r'(\w+\s\w+)(?=\sbag)', rule)
    root, children = bags[0], bags[1:]
    relationships[root] = children

def parse_rule_with_nums(rule, relationships):
    bags = re.findall(r'(\d+\s)*(\w+\s\w+)(?=\sbag)', rule)
    root = bags[0][1]
    child_bags = dict()
    for children in bags[1:]: # this is a tuple (num, color)
        child_bags[children[1]] = int(children[0]) if children[0] != "" else 0
    relationships[root] = child_bags


"""
Using relationships, find all elements that contain x and add them to contains_set. Return any added elements.
"""
def find_containing_elements(x, relationships, contains_set):
    elements = set()
    for root, children in relationships.items():
        if x in children:
            if root not in contains_set: 
                contains_set.add(root)
                elements.add(root)
    return elements


"""
Basically, look for bags that contain "shiny gold," then iteratively look for bags that contain those bags, etc. and add
all of these bags to a master set. This probably isn't the most efficient solution, but it's simple to conceptualize.

The stopping criterion is when there are no more bags that contain the bags in question. To prevent infinite loops
(A contains B contains A contains G), we only consider A if it is not already part of the master set.
"""
def day7_sol1(input):
    contains_gold = set()
    relationships = dict()
    for rule in input:
        parse_rule(rule, relationships)

    elements_to_find = {"shiny gold"}
    while len(elements_to_find) > 0:
        elements_to_find = [element for root in elements_to_find for element in find_containing_elements(root, relationships, contains_gold)]

    return len(contains_gold)
    
"""
Simple recursive solution, but requires a slightly different parse to get the num of bags. 
"""
def day7_sol2(input):
    num_bags = dict()
    relationships = dict()
    for rule in input:
        parse_rule_with_nums(rule, relationships)
    
    return find_num_bags("shiny gold", relationships, num_bags)
        

"""
Find the number of bags contained within a root bag.

Starting from the root bag, recursively find the number of bags contained in all children bags,
then do some arithmetic to compute the number of bags contained in root.
"""
def find_num_bags(root, relationships, num_bags):
    count = 0
    children = relationships[root]
    if "no other" in children:
         return 0
    else:
        for color, num in children.items():
            count += num * (1 + (num_bags[color] if color in num_bags else find_num_bags(color, relationships, num_bags)))
        num_bags[root] = count
    return count

input = load_input()

print(day7_sol1(input))
print(day7_sol2(input))