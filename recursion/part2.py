# printing 1 to n and n to 1 using recursion

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
