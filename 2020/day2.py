import re

def load_data():
    with open("input_day2.txt") as f:
        return f.read().splitlines()

def day2_sol1(input):
    count = 0
    for line in input:
        lb, ub = [int(x) for x in re.findall(r'[0-9]+', line)] # get the constraints - always going to be [0-9]-[0-9]
        letter = re.compile(re.search(r'[a-z]', line).group(0)) # get the first lowercase letter as a regex pattern
        num_occur = len(letter.findall(line)) - 1 
        count += num_occur >= lb and num_occur <= ub 
    return count

def day2_sol2(input):
    count = 0
    for line in input:
        lb, ub = [int(x) - 1 for x in re.findall(r'[0-9]+', line)] # get the constraints, and zero-index them (eg 5 literally means the 5th index, so it needs to be 4)
        letter = re.search(r'[a-z]', line).group(0) # get the first lowercase letter as a str
        password = re.search(r':\s[a-z]+', line).group(0)[2:] # get the password, discard the first 2 chars
        count += (password[lb] == letter) ^ (password[ub] == letter) 
    return count

input = load_data()
print(day2_sol1(input))
print(day2_sol2(input))
