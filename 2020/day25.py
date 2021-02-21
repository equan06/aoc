def load_input():
    with open("input_day25.txt") as f:
        return [int(x) for x in f.read().splitlines()]

def day25_pt1(input):
    "This is the Diffie-Hellman key exchange, word for word. Here p is a small prime so bruteforcing is possible."
    ckey, dkey = input
    return dkey**find(ckey) % 20201227

def day25_pt2(input):
    return "Merry Christmas!"

def find(key):
    """
    Solve 7^x = key mod 20201227 by brute force (discrete logarithm problem). 
    Note: if p-1 has a prime factorization of small primes, there's a fast algorithm to solve this (Pohlig-Hellman).
    I initially solved this just by using an online calculator and it took < 1s.
    """
    i, val = 0, 1
    while val != key:
        val = (val * 7) % 20201227
        i += 1
    return i

if __name__ == "__main__":
    input = load_input()
    print(day25_pt1(input))
    print(day25_pt2(input))