import re
def load_input():
    with open("input_day22.txt") as f:
        res = [x for x in f.read().splitlines()]
        decks = dict()
        curr = 0
        for line in res:
            if line.startswith("Player"):
                curr = int(line[7])
                decks[curr] = []
            elif line != "":
                decks[curr].append(int(line))
    return decks

def day22_pt1(deck):
    deck = {1: deck[1][:], 2: deck[2][:]}
    da, db = deck[1], deck[2]
    while len(db) > 0 and len(da) > 0:
        a = da.pop(0)
        b = db.pop(0)
        if (a < b):
            db.append(b)
            db.append(a)
        else:
            da.append(a)
            da.append(b)
    winner = 1 if len(da) > 0 else 2
    return score(deck, winner)

def day22_pt2(deck):
    deck = {1: deck[1][:], 2: deck[2][:]}
    winner = rec_game(deck)
    return score(deck, winner)

def rec_game(deck):
    "Play the game, potentially recursively. Return the player who won (1 or 2)"
    state_a, state_b = set(), set()
    da, db = deck[1], deck[2]
    while len(da) > 0 and len(db) > 0:
        if tuple(da) in state_a and tuple(db) in state_b:
            return 1    
        state_a.add(tuple(da))
        state_b.add(tuple(db))
        a = da.pop(0)
        b = db.pop(0)
        if len(da) >= a and len(db) >= b:
            winner = rec_game({1: da[:a], 2: db[:b]})
        else:
            winner = 1 if a > b else 2
        if winner == 1:
            da.append(a)
            da.append(b)
        else:
            db.append(b)
            db.append(a)
    winner = 1 if len(da) > 0 else 2
    return winner

def score(deck, winner):
    dwin = deck[1] if winner == 1 else deck[2]
    score = 0
    for i, val in enumerate(dwin[::-1]):
        score += val * (i + 1)
    return score
    
if __name__ == "__main__":
    input = load_input()
    print(day22_pt1(input))
    print(day22_pt2(input))