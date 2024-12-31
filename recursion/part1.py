"""
1. function calling itself is called recursion
2. whenever a function calls itself it creates a copy of itself in the memory stack and calls it
3. each copy of the function is in a memory stack
4. If the memory stack is full it is called stack overflow
"""
def hello():
    print("Hello World")
    hello()

def main():
    hello()
    return 0

main()
