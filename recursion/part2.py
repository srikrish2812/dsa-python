# printing 1 to n and n to 1 using recursion
""""
In recursion you do a process or computation first and then call the function again
whereas in backtracking you call the function first perform the computation.
In the display_ni_2(), first the function is called and then print() statement.
When the base case is satisified it starts printing from the latest function in the
memory stack.
"""
def display_in(i,n):
    if i==n+1: return
    print(i)
    display_in(i+1,n)

def display_ni_1(n):
    if n==0: return
    print(n)
    display_ni_1(n-1)

def display_ni_2(i,n):
    if i==n+1: return
    display_ni_2(i+1,n)
    print(i)

def main():
    display_in(i=1, n=4)
    print("\n")
    display_ni_1(4)
    print("\n")
    display_ni_2(1,4)

if __name__=="__main__":
    main()
