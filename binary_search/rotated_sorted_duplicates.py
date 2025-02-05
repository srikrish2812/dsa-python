"""
Search a Rotated Sorted Array with duplicates:
    You are given a rotated sorted array with duplicates in it
    and an integer 'k'. You need to return True if k is present
    in the array otherwise return False.

Worst Case TC = O(logn)
Average Case TC = O(n)
Best Case TC = O(logn)
SC = O(1)
"""
ARR = [5,2,4,5,5,5,5]
K = 4
N = len(ARR)
def rot_sort_dup(arr=ARR, x=K, n=N):

    low=0
    high=n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==x:
            return True
        if arr[low]==arr[mid] and arr[mid]==arr[high]:
            low=low+1
            high=high-1
        # check if leftpart is sorted
        elif arr[low]<=arr[mid]:
            if arr[low]<=x<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
        elif arr[mid]<=arr[high]:
            if arr[mid]<=x<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return False

print(rot_sort_dup(x=6))
