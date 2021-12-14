import re
from collections import defaultdict, Counter
test = True

file = "test.txt" if test else "input_day14.txt"
def load_data():
    with open(file) as f:
        top, bot = f.read().split("\n\n")
        template = top.splitlines()[0]
        rules = dict()
        for b in bot.splitlines():
            x, y = b.split(" -> ")
            rules[x] = y
    return template, rules

def day14_pt1(template, rules):
    word = template
    for _ in range(10):
        newword = ""
        for i in range(len(word) - 1):
            v = rules[word[i] + word[i + 1]]
            newword += word[i] + v
        newword += word[-1]
        word = newword
    count = Counter(word)
    sorted_count = sorted(count.values())
    return max(sorted_count) - min(sorted_count)

def day14_pt2(template, rules):
    # we only need to track the count of each pair between steps, and then the char frequency can be computed from the pairs.
    pairs = Counter()
    # initialize the pair count (step 0)
    for i in range(len(template) - 1):
        pairs[template[i:i+2]] += 1

    for _ in range(40):
        new_pairs = Counter()
        for p, freq in pairs.items():
            new_pairs[p[0] + rules[p]] += freq # count the first pair
            new_pairs[rules[p] + p[1]] += freq # count the second pair
        pairs = new_pairs

    # count the chars from the pairs
    chars = Counter()
    for p, freq in pairs.items():
        chars[p[0]] += freq
    chars[template[-1]] += 1 # the last char was never counted at all
    chars_sorted = sorted(chars.values())
    return max(chars_sorted) - min(chars_sorted)




if __name__ == '__main__':
    template, rules = load_data()
    print(day14_pt1(template, rules))
    print(day14_pt2(template, rules))


