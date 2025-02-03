"""
1. First and last position in sorted array:
    Determine the first and last occurences of integer 'k' in an array.
    If k is not found return -1 for both last and first occurences.

2. Number of Occurences:

"""

ARR = [2,5,5,5,5,6,8,9,9,11,12]
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


def optimal_first_last(arr=ARR, x=X):
    """

    """
    def first_occ(arr,x):
        ans=-1
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==x:
                ans=mid
                high = mid-1
            elif arr[mid]>x:
                high=mid-1
            else:
                low=mid+1
        return ans
    #return first_occ(ARR,X)

    def last_occ(arr,x):
        ans=-1
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==x:
                ans=mid
                low = mid+1
            elif arr[mid]<x:
                low=mid+1
            else:
                high=mid-1
        return ans
    return first_occ(ARR,X), last_occ(ARR,X)
print("Optimal Approach (first, last) =",optimal_first_last())
