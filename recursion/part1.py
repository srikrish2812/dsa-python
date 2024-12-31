"""
1. function calling itself is called recursion
2. whenever a function calls itself it creates a copy of itself in the memory stack and calls it
3. each copy of the function is in a memory stack
4. If the memory stack is full it is called stack overflow
"""
# this causes stack overflow since there is no base case/ stop condition to terminate
# def hello():
#     print("Hello World")
#     hello()

# def main():
#     hello()
#     return 0

i = 0
def hello():
    global i # tells the function to use the global variable i
    if i==4:return
    i+=1
    print("Hello")
    hello()

def main():
    hello()

if __name__ == "__main__":
    main()
