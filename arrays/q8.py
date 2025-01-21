"""
1. Maximum consecutive ones
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
