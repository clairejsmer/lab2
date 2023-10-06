# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from heapq import heappush, heappop
import heapq
from lab2_utils import TextbookStack, apply_sequence
from collections import deque

# create node that keeps track of state, flip sequence, score (g + h)
class Node(object): 
    def __init__(self, score, stack: TextbookStack, flip_sequence: list):
        self.score = score
        self.stack = stack
        self.flip_sequence = flip_sequence
        

    def print(self):
        print(self.stack)
        print(self.flip_sequence)
        print(self.score)

    def __lt__(self, other):
        return (self.score) < (other.score)


def a_star_search(stack):
    flip_sequence = []
    n = len(stack.order)
    h = find_heuristic(stack)
    start = Node(h, stack, flip_sequence)
    visited = []
    s = []
    heapq.heappush(s, start)

    while s:
        curr = heapq.heappop(s)

        # found goal state
        if curr.stack.check_ordered():
            return curr.flip_sequence
 
        # if haven't been to state before, go through neighbors and add to heap if cost (h + g) < current state's cost
        if curr not in visited:
            visited.append(curr)
            for i in range (1, n+1):
                next = curr.stack.copy()
                next.flip_stack(i)
                new_flip = curr.flip_sequence + [i]
                # calcuate heuristic for neighbor 
                next_h = find_heuristic(next) + len(new_flip)
                new = Node(next_h, next, new_flip)
                s.append(new)   
                if curr < new:
                    continue
                else:
                    heapq.heappush(s, new)
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
        elif nums[i] - nums[i - 1] == -1 and ors[i] == 1 and ors[i - 1] == 1:
            h = h + 1
        elif nums[i] - nums[i - 1] == 1 and ors[i] == 0 and ors[i - 1] == 0:
            h = h + 1
    return h 




def weighted_a_star_search(stack, epsilon=None, N=1):
    # Weighted A* is extra credit

    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #

    return flip_sequence

    # ---------------------------- #
