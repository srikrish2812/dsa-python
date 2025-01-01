"""
Reverse an array using recursion
"""

def rev_arr(i,a,n):
    if i>=n//2:return
    a[i],a[n-1-i] = a[n-i-1],a[i]
    print(a)
    rev_arr(i+1,a,n)


def main():
    a = [5,7,4,6,3,9]
    n = len(a)
    rev_arr(i=0,a=a,n=n)
    #print(a)

if __name__=="__main__":
    main()
