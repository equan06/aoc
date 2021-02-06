import re
import numpy as np
from collections import defaultdict

def load_input(test = False):
    path = "testinput_day16.txt" if test else "input_day16.txt"
    with open(path) as f:
        return f.read().strip()

def parse(input):
    "Shoutout to /u/Attitude-Certain for the clean regex. Finally getting around to using capturing groups..."
    rules = {rule: tuple(map(int, [a, b, c, d])) for rule, a, b, c, d in re.findall(r'^([\w\s]+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)$', input, flags=re.MULTILINE)}
    my_ticket, *tickets = np.array([tuple(map(int, t.split(","))) for t in re.findall(r'^([\d,]+)$', input, flags=re.MULTILINE)])
    return rules, my_ticket, tickets

def day16_pt1(input):
    "Check each ticket (row) against the rules, and sum any fields that break the rules."
    rules, my_ticket, tickets = parse(input) 
    checked = dict()
    return sum(map(lambda t: sum_rules(t, rules, checked), tickets))
    
def day16_pt2(input):
    """
    This got ugly real fast. Basic idea is to iteratively construct a mapping between each field and possible columns,
    then iteratively look for a one-to-one matching. 
    """
    rules, my_ticket, tickets = parse(input) 
    checked = dict()
    valid = np.array([t for t in filter(lambda t: check_ticket(t, rules, checked), tickets)])
    possible_matches = defaultdict(list)
    # Find a list of possible columns for each rule. 
    for rname, r in rules.items():
        for i, col in enumerate(valid.T):
            if all(check_field(field, r) for field in col):
                possible_matches[rname].append(i)

    # On a larger input, this might be faster if you sort the values in ascending order (check size 1, then size 2, etc.).
    # Note that there's likely some corner cases: consider A: [0], B: [1,2], C: [1,2]
    prod, needs_update = 1, True
    while needs_update:
        needs_update = False
        for name, p in possible_matches.items():
            if len(p) == 1:
                if name.startswith("departure"):
                    prod *= my_ticket[p[0]]
                possible_matches.pop(name)
                needs_update = True
                for v in possible_matches.values():
                    if len(v) > 1:
                        try:
                            v.remove(p[0])
                        except:
                            pass
                break
    return prod

def sum_rules(ticket, rules, checked):
    """
    Return the sum of a ticket's invalid fields. Note that the sum could return 0 even if 0 is an invalid field.
    Checked is meant to improve speed but probably doesn't matter with the input size.
    """
    res = 0
    for field in ticket:
        # Check the field against the dict
        if field in checked:
            res += field if not checked[field] else 0
            continue
        # Check the field against all rules. If any of the rules are broken, add it to the sum
        checked[field] = any(check_field(field, r) for r in rules.values())
        res += field if not checked[field] else 0
    return res

def check_ticket(ticket, rules, checked):
    "Return whether each of a ticket's fields follow at least one rule."
    return all(check_field_rules(field, rules, checked) for field in ticket)
    
def check_field_rules(field, rules, checked):
    "Check a field against all rules, and return whether it fulfills at least one of them."
    valid = checked.get(field)
    if valid is not None:
        return valid
    else:
        valid = any(check_field(field, r) for r in rules.values())
        checked[field] = valid
    return valid

def check_field(field, r):
    """Check field against r, where r is a tuple of bounds"""
    return (field >= r[0] and field <= r[1]) or (field >= r[2] and field <= r[3])

if __name__ == "__main__":
    # c = dict()
    # print(s([40, 4, 50], {"a": (1,3,5,7), "b": (6,11,33,44), "c":(13,40,45,50)}, c))
    # test = {"a":(0,1,4,19), "b":(0,5,8,19), "c":(0,13,16,19)}
    # print(check_col([3, 15, 5], test))
    # print(check_col([9, 1, 14], test))
    # print(check_col([18, 5, 9], test))

    input = load_input()
    print(day16_pt1(input))
    print(day16_pt2(input))