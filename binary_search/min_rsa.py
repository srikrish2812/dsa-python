"""
1. Find the minimum in rotated sorted array

2. Find the minimum rotations in the array
"""
ARR = [6,7,8,9,3,4,5]
def min_rot_sort(arr=ARR):
    """
    Whenever rotated sorted array is given it always has a sorted part.
    First we check for the sorted part and proceed with the logic according
    to the question.

    TC = O(logn)
    SC = O(1)
    """
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

def min_rotations(arr=ARR):
    """
    No. of min rotations = index of the min element in the rot sorted arr
    TC = O(logn)
    SC = O(1)
    """

    low = 0
    n = len(arr)
    high=n-1
    ans = float("inf")
    ans_index= -1
    while low<=high:
        mid = low + (high-low)//2
        if arr[low]<=arr[mid]:
            if arr[low]<=ans:
                ans = arr[low]
                ans_index = low
            low= mid+1
        elif arr[mid]<=arr[high]:
            if arr[mid]<=ans:
                ans=arr[mid]
                ans_index = mid
            high=mid-1
    return ans_index

print(f"Minimum rotations = {min_rotations()}")
