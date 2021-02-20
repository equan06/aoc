def load_input():
    with open("input_day23.txt") as f:
        return [int(y) for y in [x for x in f.read().splitlines()][0]]

def day23_pt1(input):
    "Nice and compact solution for a nice and small input."
    input = input[:]
    lb, ub = min(input), max(input)
    for _ in range(100):
        curr = input.pop(0)
        val = ub if curr - 1 < lb else curr - 1
        while val in input[:3]:
            val = ub if val - 1 < lb else val - 1
        i = input.index(val)
        input = input[3:i+1] + input[:3] + input[i+1:] + [curr]
    idx = input.index(1)
    return str.join("", [str(x) for x in input[idx + 1:] + input[:idx]])

def day23_pt2(input, list_size=10**6, num_iter=10**7, day1_res=False):
    """Use a circular linked list with a third back pointer to node val - 1.
    This avoids linear search during each iter."""
    lst = DLL(input, list_size)
    for _ in range(num_iter):
        curr = lst.curr
        val = curr.back 
        while val in {curr.next, curr.next.next, curr.next.next.next}:
            val = val.back
        # save the location after the tuple
        temp = val.next
        # link val to the first elem of tuple
        val.next = curr.next  
        curr.next.prev = val 
        # link curr to the elem after the third elem of tuple
        last_tuple = curr.next.next.next 
        curr.next = last_tuple.next
        # link the third elem of tuple to the elem after val
        last_tuple.next = temp
        temp.prev = last_tuple  
        lst.curr = lst.curr.next

    if day1_res:
        res = []
        curr = lst.one.next
        while curr != lst.one:
            res.append(curr.val)
            curr = curr.next
        return str.join(",", [str(x) for x in res])
    else:
        curr = lst.one.back
        return lst.one.next.val * lst.one.next.next.val
    

class Node:
    def __init__(self, val):
        self.val = val

    def link_next(self, node):
        self.next = node

    def link_prev(self, node):
        self.prev = node

    def link_back(self, node):
        self.back = node
    
    def __str__(self):
        return f"val:{self.val} next:{self.next.val} prev:{self.prev.val} back:{self.back.val}"

class DLL:
    def __init__(self, input, size):
        init = dict()
        first = Node(input[0])
        prev, init[input[0]], self.curr = first, first, first
        for i in input[1:]:
            curr = Node(i)
            init[i] = curr
            prev.next = curr # setup two-way link
            curr.prev = prev
            prev = curr
        # first and last have not been linked, nor have min and max
        for val, node in init.items():
            if val == min(input): 
                self.one = node # need to link min to max
                continue
            node.back = init[val - 1]
        self.largest = init[max(input)]
        self.len = len(input)
        # at beginning, prev is still the last node in input
        while self.len < size:
            self.len += 1
            curr = Node(self.len)
            prev.next = curr
            curr.prev = prev
            # link back to max if starting the sequence
            curr.back = self.largest if self.len == len(input) + 1 else prev 
            self.largest = curr if self.len > self.largest.val else self.largest
            prev = curr
        # if no additional nodes, then link first and last 
        prev.next = first
        first.prev = prev 
        self.one.back = self.largest # link min to max
        self.len = size

    def __str__(self):
        res = []
        i = 0
        curr = self.curr
        while i < self.len:
            res.append(str(curr.val))
            curr = curr.next
            i += 1
        return str.join(", ", res)
       
if __name__ == "__main__":
    input = load_input()
    print(day23_pt1(input))
    print(day23_pt2(input))


