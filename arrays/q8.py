"""
1. Maximum consecutive ones
2. Find missing number
"""

def maxcon_ones(arr=[1,0,1,1,0,1,1,1,1,0]):
    """
    TC=O(n)
    SC = O(1)
    """
    cur=0
    max=0
    for i in range(len(arr)):
        if arr[i]==1:
            cur+=1
            if cur>max:
                max=cur
        else:
            cur=0
    return max

print(maxcon_ones())


def find_miss_brute(arr=[5,3,1,6,2],n=6):
    """
    TC = O(n^2)
    SC = O(1)
    """
    for i in range(1,n+1):
        present=0
        for j in range(0,n-1):
            if i==arr[j]:
                present=1
                break
        if present==0: return i
