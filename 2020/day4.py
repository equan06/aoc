import re

def load_input():
    with open("input_day4.txt") as f:
        return f.read().split("\n\n") # return a list of passport strings


"""
Assuming that each passport is parsed as a string, simply count the number of matching
fields (3 lowercase letters followed by :).  
"""
def day4_sol1(input):
    count = 0
    for passport in input:
        fields = re.findall(r'[a-z]{3}:', passport)
        if len(fields) == 8 or (len(fields) == 7 and "cid:" not in fields):
            count += 1
    return count
        

def day4_sol2(input):
    count = 0
    for passport in input:
        fields = re.findall(r'[a-z]{3}:', passport)
        if len(fields) == 8 or (len(fields) == 7 and "cid:" not in fields):
            count += validate(passport)
    return count


"""
Manually go through each passport? This got ugly real quick

It would be good to refactor this later - instead of doing it line by line,
just set up a mapping between each 3 letter field and a specific validation function
    
A probably cleaner way to split is to 
first split by \n\n, then split by \s, then split by : to get the key and the value.

I instead split by \n\n then [\n\s:], and then iterate over consecutive elements 0,1 then 2,3 ...
"""
def validate(passport):
    is_valid = 1
    fields = re.split('[\n\s:]', passport) 
    for i in range(len(fields)): 
        if i % 2 == 0:
            field_val = fields[i+1]
            if fields[i] == "byr":
                is_valid = len(field_val) == 4 and field_val >= "1920" and field_val <= "2002"
            elif fields[i] == "iyr":
                is_valid = len(field_val) == 4 and field_val >= "2010" and field_val <= "2020"
            elif fields[i] == "eyr":
                is_valid = len(field_val) == 4 and field_val >= "2020" and field_val <= "2030"
            elif fields[i] == "hgt":
                if field_val[-2:] == "in":
                    is_valid = field_val[:-2] >= "59" and field_val[:-2] <= "76"
                elif field_val[-2:] == "cm":
                    is_valid = field_val[:-2] >= "150" and field_val[:-2] <= "193"
                else:
                    is_valid = 0
            elif fields[i] == "hcl":
                if field_val[0] == "#":
                    val = re.match(r'[A-Za-z0-9]+', field_val[1:])
                    is_valid = val != None and len(val.group(0)) == 6
                else:
                    is_valid = 0
            elif fields[i] == "ecl":
                is_valid = re.match(r'amb|blu|brn|gry|grn|hzl|oth', field_val)
            elif fields[i] == "pid":
                val = re.match(r'[0-9]+', field_val)
                is_valid = val != None and len(val.group(0)) == 9
            if not is_valid:
                return 0
    return 1
        
input = load_input()
print(day4_sol1(input))
print(day4_sol2(input))