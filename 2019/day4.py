
def load_input():
    input = "172930-683082"
    return [int(x) for x in input.split('-')]

def solve_4pt1(input):
    a, b = input
    return len([x for x in get_consec(6) if x >= a and x <= b and has_repeats(x)])

def solve_4pt2(input):
    a, b = input
    return len([x for x in get_consec(6) if x >= a and x <= b and has_repeats_special(x)])
    
def get_consec(num_digit = 1):
    """
    A faster implementation of getting nondecreasing strings of a certain length, building the list from the bottom up and simply appending digits to the left.
    """
    master = set()
    increasing_prev = set()
    for i in range(num_digit):
        increasing = set()
        if len(increasing_prev) == 0:
            increasing_prev = set(range(10))
        else:
            for x in increasing_prev:
                for num in range(10):
                    if (str(num) <= str(x)[0]):
                        increasing.add(int(str(num) + str(x)))
            increasing_prev = increasing
        for j in increasing_prev:
            master.add(j)
    return set(x for x in master if len(str(x)) == num_digit)


def get_consec_slow(n = 1):
    """Brute force approach is rather slow."""
    master = set()
    for i in range(10**(n-1), 10**n):
        num_str = str(i)
        consec = True
        for j in range(len(num_str) - 1):
            if num_str[j] > num_str[j + 1]:
                consec = False
                break
        if consec:
            master.add(i)
    return master

def has_repeats(num):
    """Return whether the num has repeating digits."""
    num_str = str(num)
    for i in range(len(num_str) - 1):
        if num_str[i] == num_str[i + 1]:
            return True
    return False

def has_repeats_special(num):
    """This is ugly but gets the job done. Counts the length of each run of digits, and breaks early if length 2 run is found."""
    num_str = str(num)
    num_consec = 1
    prev = ""
    for i in range(len(num_str)):
        if num_str[i] == prev:
            num_consec += 1
        else:
            if num_consec == 2:
                return True
            num_consec = 1
        prev = num_str[i]
    return num_consec == 2

if __name__ == "__main__":
    input = load_input()
    print(solve_4pt1(input))
    print(solve_4pt2(input))