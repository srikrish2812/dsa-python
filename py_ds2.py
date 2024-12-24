from collections import deque

my_deque = deque([1,2,3])
my_deque.append(4)
my_deque.appendleft(0)

print(my_deque)

print(my_deque.pop())
print(my_deque.popleft())

my_deque.extend([4,5,6,7])
my_deque.extendleft([0,-1,-2])
print(my_deque) # deque([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7])

my_deque.rotate(2)

for element in my_deque:
    print(element, end=" ")
