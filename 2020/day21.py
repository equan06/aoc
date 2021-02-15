import re
from functools import reduce

def load_input():
    with open("input_day21.txt") as f:
        return [[re.findall("\w+", x) for x in line.split("contains")] for line in f.read().splitlines()] 
        
def parse(input):
    ingreds = set()
    allergy = set()
    for line in input:
        ingreds.update({k for k in line[0]})
        allergy.update({k for k in line[1]})
    return ingreds, allergy

def day21_pt1(foods):
    """
    For each allergy, find all the ingredients that could contain it (intersection).
    Then take the difference. 
    """
    ingreds, allergy = parse(foods)
    temp = set()
    for a in allergy:
        temp = temp.union(reduce(set.intersection, (set(f[0]) for f in foods if a in f[1])))
    not_contains = ingreds.difference(temp)
    return sum(len(not_contains.intersection(f[0])) for f in foods)

def day21_pt2(foods):
    """
    Filter the ingredients if they contain an allergy. Then iteratively search for 1 to 1
    mappings between ingredients and allergies. Very similar to Day 16 pt2.
    """
    ingreds, allergy = parse(foods)
    temp = set()
    for a in allergy:
        temp = temp.union(reduce(set.intersection, (set(f[0]) for f in foods if a in f[1])))
    not_contains = ingreds.difference(temp)
    for f in foods: # careful: f[0] is now a set!
        f[0] = set(f[0]).difference(not_contains) 
    adict = dict()
    while len(allergy) > 0:
        for a in allergy:
            # take the intersection of all ingreds containing a
            cands = set() 
            for f in foods:
                if a in f[1] and len(f[0]) > 0:
                    cands = f[0] if len(cands) == 0 else cands.intersection(f[0])
            # exact match found, so remove that ingredient from all other lists
            if len(cands) == 1: 
                adict[a], = cands # unpack a singleton 
                foods = [i for i in map(lambda f: [f[0].difference(cands), f[1]], foods)]
                allergy.remove(a)
                break
    return str.join(",", [adict[i] for i in sorted(adict)])

if __name__ == "__main__":
    input = load_input()    
    print(day21_pt1(input))
    print(day21_pt2(input))
