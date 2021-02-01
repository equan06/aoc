import re

def load_input():
    with open("input_day14.txt") as f:
        return [x for x in f.read().splitlines()]

def make_bit_on(idx):
    return lambda x: x | (1<<idx)

def make_bit_off(idx):
    return lambda x: x & ~(1<<idx)

def day14_pt1(input):
    to_run = []
    nonzeros = dict() # store the addresses of nonzero values only
    for line in input:
        if line[:3] == "mem":
            addr, val = [int(x) for x in re.findall(r'\d+', line)]
            for f in to_run:
                val = f(val)
            if val != 0:
                nonzeros[addr] = val
            else:
                nonzeros.pop(addr, val)
        else:
            to_run = []
            mask = re.search(r'[01X]+', line).group(0)
            for idx, val in enumerate(mask[::-1]):
                if val == "1":
                    to_run.append(make_bit_on(idx))
                elif val == "0":
                    to_run.append(make_bit_off(idx))
    return sum(nonzeros.values())

"""
There's a bug somewhere in this code - too lazy to find it, so rewrote it below...
Works on the test input, fails on the actual input. I'm guessing it's the bit operations...
"""
# def day14_pt2(input):
#     to_run, floats, permutes = [], [], []
#     mem = dict()
#     for line in input:
#         if line[:3] == "mem":
#             addr, val = [int(x) for x in re.findall(r'\d+', line)]
#             for f in to_run:
#                 addr = f(addr)
#             addrs = generate_addr(addr, floats, permutes)
#             for a in addrs:
#                 mem[a] = val
#         else:
#             to_run, floats, permutes = [], [], []
#             mask = re.search(r'[01X]+', line).group(0)
#             for idx, val in enumerate(mask[::-1]):
#                 if val == "1":
#                     to_run.append(make_bit_on(idx))
#                 elif val == "X":
#                     floats.append(idx)
#             permutes =  [format(i, f"0{len(floats)}b") for i in range(2**len(floats))]
#     return sum(mem.values())

# def generate_addr(addr, floats, permutes):
#     res = []
#     for p in permutes:
#         for bit, idx in zip(p, floats):
#             if bit:
#                 addr = addr | (1<<idx)
#             else:
#                 addr = addr & ~(1<<idx)
#         res.append(addr)
#     return res

def day14_pt2_2(input):
    mem = dict()
    ones, floats, permutes = [], [], []
    for line in input:
        if line[:4] == "mask":
            ones, floats, permutes = [], [], []
            mask = re.search(r'[01X]+', line).group(0)
            for idx, val in enumerate(mask[::-1]): 
                if val == "1":
                    ones.append(idx)
                elif val == "X":
                    floats.append(idx)
            permutes = [format(i, f"0{len(floats)}b") for i in range(2**len(floats))]
        else:
            addr, val = [int(x) for x in re.findall(r'\d+', line)]
            addr_str = format(addr, "038b")[::-1] # reverse the binary str (index 0 is now left bit)
            addr_str = apply_ones(addr_str, ones)
            addrs = apply_mask(addr_str, floats, permutes)
            for a in addrs:
                mem[a] = val
    return sum(mem.values())

"""
Replace chars with 1 for each index in ones.
"""
def apply_ones(addr, ones):
    for idx in ones:
        addr = addr[:idx] + "1" + addr[idx + 1:]
    return addr

"""
Return a list of all permutations of address, permuted at the indices given by floats using binary digits only.
Permutes is a list of all bitstrings of size len(floats).
"""
def apply_mask(addr, floats, permutes):
    res = []
    for p in permutes:
        for bit, idx in zip(p, floats):
            addr = addr[:idx] + bit + addr[idx + 1:]
        res.append(addr)
    return res
            
    
if __name__ == "__main__":
    input = load_input()
    # test = ["mask = 000000000000000000000000000000X1001X",
    # "mem[42] = 100",
    # "mask = 00000000000000000000000000000000X0XX",
    # "mem[26] = 1"]
    print(day14_pt1(input))
    # print(day14_pt2(input))
    print(day14_pt2_2(input))



