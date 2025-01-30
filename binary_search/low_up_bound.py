"""
1. Lower Bound: Find i s/t arr[i]>=x and return i. If all the elements
in arr are less than x then return len(arr)
2. Upper Bound
"""
ARR = [2,3,5,5,6,7,7,7,10,12]
X = 8
def lower_bound(arr=ARR,x=X):
    """
    TC = O(logn)
    SC = O(1)
    """
    n = len(ARR)
    low = 0
    high = n-1
    ans = n
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>=x:
            ans = mid
            high = mid-1
        elif arr[mid]<x:
            low=mid+1
    return ans
print(lower_bound())
