"""
Find the peak element:
    Given an array of length 'n' find the element that is greater than
    its adjacent neighbors
"""
ARR = [1,2,3,4,5,6,7,8,4,2,1]
def brute_appr(arr=ARR):
    n = len(arr)
    for i in range(n):
        if i==0 and arr[0]>arr[1]:
            return i
        elif i==n-1 and arr[n-1]>arr[n-2]:
            return i
        elif arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            return i
    return -1
print(f"Using Linear Search Approach: {brute_appr()}")
