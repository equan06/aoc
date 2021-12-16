import sys
from functools import reduce

def load_data(file):
    with open(file) as f:
        return str(f.read())

map = """0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111"""

hex = dict()
for line in map.splitlines():
    a, b = line.split(" = ")
    hex[a] = b

op = {
    0: lambda l: sum(l),
    1: lambda l: reduce(lambda x, y: x * y, l),
    2: lambda l: min(l),
    3: lambda l: max(l),
    5: lambda l: 1 if l[0] > l[1] else 0,
    6: lambda l: 1 if l[0] < l[1] else 0,
    7: lambda l: 1 if l[0] == l[1] else 0,
}

def day16_sol1(input):
    # convert hex to binary
    bin = ""
    for i in input:
        bin += hex[i]
    nums = []
    parse_packet(bin, nums)
    return sum(int(b, 2) for b in nums)

def day16_sol2(input):
    bin = ""
    for i in input:
        bin += hex[i]
    nums = []
    return parse_packet(bin, nums)[1]


def parse_packet(bin, nums):
    if int(bin, 2) == 0: # if the binary rep is 0, then exit
        return len(bin), 0
    val = 0
    i = 0
    version = bin[i:i+3] 
    i += 3
    type_id = bin[i:i+3]
    i += 3
    nums.append(version)
    if type_id == '100': # 4 = literal
        nums = []
        read = True
        literal = ""
        while read:
            if bin[i] == '0': read = False
            literal += bin[i+1:i+5]
            i += 5
        val = int(literal, 2)
    else: # operator
        length = bin[i]
        i += 1
        sub_packets = []
        if length == '0':
            total_len = int(bin[i:i+15], 2)
            i += 15
            pck_end = i + total_len
            # parse the immediate subpackets
            while i < pck_end:
                pck_len, pck = parse_packet(bin[i:pck_end], nums)
                sub_packets.append(pck)
                i += pck_len
        else:
            num_pck = int(bin[i:i+11], 2)
            i += 11
            count = 0
            while count < num_pck:
                pck_len, pck = parse_packet(bin[i:], nums)
                sub_packets.append(pck)
                i += pck_len
                count += 1
        
        # apply the operator
        val = op[int(type_id,2)](sub_packets)

    return i, val

if __name__ == "__main__":
    file = f"{sys.argv[1]}.txt" if len(sys.argv) > 1 else "input_day16.txt"
    print(file)
    input = load_data(file)
    print(day16_sol1(input))
    print(day16_sol2(input))