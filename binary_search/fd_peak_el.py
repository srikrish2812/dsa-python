"""
Find the peak element:
    Given an array of length 'n' find the element that is greater than
    its adjacent neighbors
"""
ARR = [1,2,3,4,5,6,7,8,4,2,1]
def brute_appr(arr=ARR):
    n = len(arr)
    if n==1:
        return 0
    for i in range(n):
        if i==0 and arr[0]>arr[1]:
            return 0
        elif i==n-1 and arr[n-1]>arr[n-2]:
            return i
        elif arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            return i
    return -1
print(f"Using Linear Search Approach: {brute_appr()}")


def opt_appr(arr=ARR):
    n =len(arr)
    if n==1: return 0
    if arr[0]>arr[1]: return 0
    if arr[n-1]>arr[n-2]: return n-1

    low=1
    high=n-2
    while low<=high:
        mid = low+(high-low)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]>arr[mid-1]:
            low = mid+1
        else:
            high=mid-1
    return -1
print(f"Using Optimal Approach: {opt_appr()}")
