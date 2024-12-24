"""
The deque class in Python provides a balanced
and efficient implementation for frequent insertions
and deletions at both ends. It is optimized for fast
appends and pops from both ends.


"""
from collections import deque

my_deque = deque([1,2,3])
my_deque.append(4)
my_deque.appendleft(0)

print(my_deque)
print(my_deque[3]) # 3 :accessing elements is not efficient in deque compared to lists
print(my_deque.pop()) # 4
print(my_deque.popleft()) # 0

my_deque.extend([4,5,6,7]) # [1, 2, 3, 4, 5, 6, 7]
my_deque.extendleft([0,-1,-2]) # [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
print(my_deque) # deque([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7])

my_deque.rotate(2) # rotate deuqe 2 steps to right

for element in my_deque:
    print(element, end=" ")
print()
my_deque[4] = -100
print(my_deque)
