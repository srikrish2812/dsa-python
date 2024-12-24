from collections import deque

stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print("Stack after pushing elements:")
print(stack)
print("\nElements popped from the stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

"""
Using deque for a stack ensures O(1) time complexity
for both push and pop operations, unlike lists which
can have varying performance for pop operations depending
on the size of the list. It is optimized for fast appends
and pops from both ends.
"""

print("--"*10)
print("    Using deque")
print("--"*10)
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after pushing elements:")
print(stack)
print("\nElements popped from the stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("\nStack after popping elements:")
print(stack)
