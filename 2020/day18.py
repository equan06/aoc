def load_input():
    with open("input_day18.txt") as f:
        return [x for x in f.read().replace(" ", "").splitlines()]

def day18_pt1(input):
    return sum(map(parse, input))

def day18_pt2(input):
    return sum(map(parse, map(preprocess, input)))

def parse(line):
    "Assuming line is nonempty, compute the result while ignoring order of operations for + and *."
    i = 0
    curr = line[0]
    if len(line) == 1:
        return int(curr)
    while i+2 < len(line):
        if line[i] == "(":
            end = find_end_bracket(line[i:])
            curr = parse(line[i+1:i+end])
            i = i+end # advance to index of end bracket
        else:
            op = line[i+1]
            b = line[i+2]
            if b == "(":
                end = find_end_bracket(line[i+2:]) # end is the offset from i+2
                b = parse(line[i+3:i+2+end])
                curr = opr(curr, op, b)
                i = i+2+end # advance to index of end bracket
            else:
                curr = opr(curr, op, b)
                i += 2 # advance to index of b
    return curr

def opr(a, op, b):
    return int(a) * int(b) if op == "*" else int(a) + int(b)
    
def find_end_bracket(line):
    "Find the end index of the right bracket corresponding to the left bracket at index 0."
    if line[0] == "(":
        num_left = 0
        for i, char in enumerate(line):
            if char == ")" and num_left == 1:
                return i
            elif char == ")":
                num_left -= 1
            elif char == "(":
                num_left += 1
    return -1

def preprocess(line):
    "Basically, insert parentheses before/after multiplications. This forces additions to be evaluated before multiplications."
    return "(" + line.replace("(", "((").replace(")", "))").replace("*", ")*(") + ")"
    
        
assert parse("1+3*4+(5*2)") == 26
assert parse("(1+(1*4))*2+3") == 13
assert parse(preprocess("(1+(1*4))*2+3")) == 25

input = load_input()
print(day18_pt1(input))
print(day18_pt2(input))