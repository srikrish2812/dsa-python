"""
Square root of n
"""

def brute_appr(n):
    """
    TC = O(sqrt(n))
    SC = O(1)
    """
    ans = None
    for i in range(n//2+1):
        if i*i<=n:
            ans=i
        else:
            break
    return ans
print("Brute Force Approach: ",brute_appr(4))

def optimal_appr(n):
    low, high=0,n
    ans=-1
    while low<=high:
        mid = low +(high-low)//2
        if mid*mid>n:
            high=mid-1
        else:
            ans=mid
            low=mid+1
    return ans
print(f"Using Optimal Approach: {optimal_appr(5)}")
