"""
1. Search Insert Position Problem: Given a target value and a sorted array find
the position where the target value is present in the array. If it is not
present then find the index where iit should be placed.

2. Ceil and Floor: Given a sorted array along with a given integer 'x' the task
is to determine both the floor and ceil of x within the array denoted as.
Floor of x is the largest element in the array that is smaller than or equal
to x. Ceil of x is the smallest element in the array that is greater than or
equal to x.
"""

ARR = [4,5,6,9]
M = 7
def search_insert(arr=ARR, m=M):
    """
    This problem is same as lower bound problem. We need to find the
    smallest i such that arr[i]>=target and insert it at index i

    TC = O(logn)
    SC = O(1)
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
print("Search Insert Problem",search_insert())

X=16
ARR = [5,10,10,15,15,20,25]
N = len(ARR)
def ceil(arr=ARR,x=X,n=N):
    """
    return -1 if there is no ceil value of x in the array
    """
    low =0
    high =n-1
    ceil = -1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ceil = arr[mid]
            high = mid-1
        else:
            low=mid+1
    return ceil

print(f"Ceil value = {ceil()}")

def floor(arr=ARR,x=X,n=N):
    low = 0
    high =n-1
    floor=-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<=x:
            floor=arr[mid]
            low=mid+1
        else:
            high=mid-1
    return floor
print(f"Floor Value = {floor()}")
