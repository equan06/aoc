import ast
# step 1: add x + y = [x, y]
# step 2: repeatedly reduce until no reductions possible
# step 2a: if pair is nested 4x (depth of 5), explode (add left to leftmost, add right to rightmost, and replace pair with 0)
# step 2b: if number >= 10, split (10 = [5, 5], 11 = [5, 6])
def load_data():
    with open("input_day18.txt") as f:
        nums = [ast.literal_eval(num) for num in f.read().splitlines()]
    return nums


def add(x, y):
    """Add two snailfish numbers."""
    new_sum = [x, y]
    # while True:

def check_explode(x, depth = 0):
    if not isinstance(x, list):
        return (None, None)
    elif depth == 4:
        return x

    exploded_left = check_explode(x[0], depth + 1)
    if exploded_left != (None, None):
        if not None in exploded_left:
            x[0] = 0
        if exploded_left[1] is not None:
            if isinstance(x[1], list):
                assign_leftmost(x[1], exploded_left[1])
            else:
                x[1] += exploded_left[1]

        exploded_left[1] = None
        return exploded_left

    exploded_right = check_explode(x[1], depth + 1)
    if exploded_right != (None, None):
        if not None in exploded_right:
            x[1] = 0
        if exploded_right[0] is not None:
            if (isinstance(x[0], list)): 
                assign_rightmost(x[0], exploded_right[0])
            else:
                x[0] += exploded_right[0]

        exploded_right[0] = None
        return exploded_right

    return (None, None)
    
def assign_rightmost(x, val):
    # add val to the rightmost value in a list
    curr = x
    while isinstance(curr[1], list):
        curr = curr[1]
    curr[1] += val
    print(x)

def assign_leftmost(x, val):
    curr = x
    while isinstance(curr[0], list):
        curr = curr[0]
    curr[0] += val
    print(x)
    
    

test = [[[[[9,8],1],2],3],4]
check_explode(test)
print(test)

test = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
check_explode(test)
print(test)