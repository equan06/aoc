import re
from itertools import permutations

def load_data():
    with open("input_day08.txt") as f:
        return [re.findall(r"\w+", x) for x in f.read().splitlines()]

digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
}

word_to_digit = {v:k for k,v in digits.items()}

def bruteforce(input):
    output = 0
    for line in input:
        before, after = line[:10], line[10:]
        # find a permutation fxn between the current line's config and the default config
        for p in permutations("abcdefg"):
            valid = True
            perm = {k: v for k, v in zip(p, "abcdefg")}
            for word in before:
                pattern = ""
                for char in word:
                    pattern += perm[char]
                if "".join(sorted(pattern)) not in digits.values(): 
                    valid = False
                    break
            if not valid: continue
            # assume the permutation is valid, and index into the word -> digit mapping
            num = [word_to_digit["".join(sorted(perm[char] for char in word))] for word in after]
            output += int("".join([str(d) for d in num]))
            break
    return output

if __name__ == '__main__':
    input = load_data()
    print(bruteforce(input))