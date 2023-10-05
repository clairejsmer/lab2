# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from heapq import heappush, heappop
import heapq
from lab2_utils import TextbookStack, apply_sequence
from collections import deque

class Node(object): 
    def __init__(self, stack: TextbookStack, flip_sequence: list, g=0, h=0):
        self.stack = stack
        self.flip_sequence = flip_sequence
        self.g = g
        self.h = h

    def print(self):
        print(self.stack)
        print(self.flip_sequence)
        print(self.g)
        print(self.h)

    def comp(self, other):
        return (self.g + self.h) < (other.g + other.h)



def a_star_search(stack):
    flip_sequence = []
    n = len(stack.order)
    curr = stack
    g = find_heuristic(curr)
    curr = [(stack, flip_sequence, g)]
    s = []
    s.append(curr)
    # start = Node(stack, flip_sequence, 0, find_heuristic(stack))
    

    visited = []
    heapq.heappush(s, curr) 

    while s:

        c = heapq.heappop(s)
        curr = c[0]
        currflip = c[1]
        currg = c[2]

        if curr.check_ordered():
            print("FOUND SOLUTION")
            print("order: ", curr.order)
            print("orientation: ", curr.orientations)
            print("flip sequence: ", currflip)
            return currflip


        if curr not in visited:
            visited.append(curr)
            for i in range (1, n+1):
                next = curr.copy()
                next.flip_stack(i)
                new_flip = currflip + [i]
                h = find_heuristic(next) + len(new_flip)
                if currg > h:
                    print("order: ", next.order)
                    print("orientations: ", next.orientations)
                    new = [(next, new_flip, h)]
                    s.append(new)
                    heapq.heappush(s, new)
    print("ERROR RETURN")       
    return flip_sequence   



# estimates h value based on piazza rules
def find_heuristic(stack):
    h = 0
    nums = stack.order
    ors = stack.orientations
    for i in range(1, len(stack.order)):
        if abs(nums[i] - nums[i - 1]) > 1:
            h = h + 1
        elif ors[i] != ors[i - 1]:
            h = h + 1
        elif nums[i] - nums[i - 1] == -1 & ors[i] == 1 & ors[i - 1] == 1:
            h = h + 1
        elif nums[i] - nums[i - 1] == 1 & ors[i] == 0 & ors[i - 1] == 0:
            h = h + 1
    return h 




def weighted_a_star_search(stack, epsilon=None, N=1):
    # Weighted A* is extra credit

    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #

    return flip_sequence

    # ---------------------------- #
