"""
1. Search Insert Position Problem: Given a target value and a sorted array find
the position where the target value is present in the array. If it is not
present then find the index where iit should be placed.
"""

ARR = [4,5,6,9]
M = 7
def search_insert(arr=ARR, m=M):
    """
    This problem is same as lower bound problem. We need to find the
    smallest i such that arr[i]>=target and insert it at index i
    """
    low = 0
    n = len(arr)
    high = n-1
    ans = None
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>=m:
            ans = mid
            high=mid-1
        else:
            low=mid+1
    return ans
print(search_insert())
