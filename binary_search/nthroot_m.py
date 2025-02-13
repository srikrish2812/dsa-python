"""

Find the nth root of an integer
"""

def power(k,n):
    ans=k
    for _ in range(1,n):
        ans*=k
    return ans

def brute_force(n,m):
    """
    The power function will run for n times and the
    below for loop runs k-times where k**n==m => k = m**(1/n)

    TC = O(n*m^(1/n))
    SC = O(1)
    """
    for i in range(m):
        if power(i,n)==m:
            return i
        elif power(i,n)>m:
            return -1

print(f"Using brute force: {brute_force(3,64)}")


def opt_appr(n,m):
    """
    TC = O(n*logm)
    SC = O(1)
    """
    low =1
    high = m
    while low<=high:
        mid = low + (high-low)//2
        if power(mid,n)==m:
            return mid
        elif power(mid,n)>m:
            high=mid-1
        else:
            low=mid+1
    return -1

print(f"Using Optimal Approach: {opt_appr(3,62)}")

"""
We can modify power function by giving it k,n,m. In this way
we do not exactly calculate the power because calculating powers of
large numbers throws overflow errors.
"""

def new_power(mid, n,m):
    ans=1
    for _ in range(n):
        ans = ans*mid
        # return 1 if ans>m
        if ans>m:
            return 1
    if ans==m:
        return 0
        # return -1 if ans<m
    else:
        return -1

def new_opt(n,m):
    low= 1
    high=m

    while low<=high:
        mid = low + (high-low)//2

        if new_power(mid,n,m)==0:
            return mid
        if new_power(mid,n,m)==-1:
            low = mid+1
        else:
            high=mid-1
    return -1

print(f"Using modified power function that takes care of memory issues in finding the power of number {new_opt(3,64)}")
