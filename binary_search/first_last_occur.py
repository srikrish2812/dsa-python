"""
1. First and last position in sorted array:
    Determine the first and last occurences of integer 'k' in an array.
    If k is not found return -1 for both last and first occurences.

2. Number of Occurences:

"""

ARR = [2,5,5,5,6,8,9,9,11,12]
X = 5

def brute_first_last(arr=ARR, x=X):
    """
    TC = O(n)
    SC = O(1)
    """
    first = -1
    last=-1
    for i in range(len(arr)):
        if arr[i]==x:
            if first==-1: first=i
            last=i
    return first, last

print(f"Brute Force (first, last) = {brute_first_last()}")
