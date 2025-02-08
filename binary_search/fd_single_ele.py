"""
Find the element that occurs just once in the  sorted array
"""
ARR = [2,2,4,4,6,6,7,9,9]
def brute_appr(arr=ARR):
    """
    TC = O(n)
    SC = O(1)
    """
    n = len(arr)
    if n==1: return arr[0]
    if arr[0]!=arr[1]: return arr[0]
    if arr[n-2]!=arr[n-1]: return arr[n-1]

    for i in range(1,n-1):
        if arr[i]!=arr[i-1] and arr[i]!=arr[i+1]:
            return arr[i]
    return -1

print(brute_appr())


def optimal_appr(arr=ARR):

    """
    1. Before the single element the indices of the pairs are (even,odd)
    2. After the single element the indices of the pairs are (odd, even)

    """
    n = len(arr)
    if n==1: return arr[0]
    if arr[0]!=arr[1]: return arr[0]
    if arr[n-2]!=arr[n-1]: return arr[n-1]

    low = 1
    high = n-2
    while low<=high:
        mid = low + (high-low)//2

        if arr[mid]!=arr[mid-1] and arr[mid]!= arr[mid+1]:
            return arr[mid]
        if (mid%2==1 and arr[mid]==arr[mid-1]) or (mid%2==0 and arr[mid]==arr[mid+1]):
            low= mid+1
        else:
            high=mid-1
    return -1

print('Using Optimal Approach:',optimal_appr())
