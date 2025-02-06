"""
1. Find the minimum in rotated sorted array
"""
ARR = [6,7,8,9,3,4,5]
def min_rot_sort(arr=ARR):

    low = 0
    n = len(arr)
    high=n-1
    ans = float('inf')
    while low<=high:
        mid = low + (high-low)//2
        if arr[low]<=arr[mid]:
            ans= min(ans, arr[low])
            low= mid+1
        elif arr[mid]<=arr[high]:
            ans= min(ans, arr[mid])
            high=mid-1
    return ans

print("Minimum element =",min_rot_sort())
