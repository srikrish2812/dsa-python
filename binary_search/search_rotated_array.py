"""
Search in Rotated Sorted Array:
    You are given an array arr, integer k and size of the array n.
    The array is rotated at index and your task is to find out if
    it contains the integer k and return it's index. If the array
    doesn't contain the index then return -1. There are no duplicates
    in the array.

input: arr=[8,2,4,6,7] and k=4 then output:2
Here the array [2,4,6,7,8] is rotated at index 4
"""
ARR = [10,11,12,4,5,6,7,8,9]
N = len(ARR)
K = 12
def search_rotated_sorted(arr=ARR,k=K,n=N):
    """
    In a rotated sorted array, one half is sorted and the other is
    unsorted relative to the another half. Using this property, we
    first check for the sorted half and check if it has the element.

    Steps:
        1. Idenitfy the sorted half and
        2. Check if the sorted half has the element k and update
        the low and high appropriately
    """

    low = 0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==k: return mid
        # check if left  is sorted
        elif arr[low]<=arr[mid]:
            if arr[low]<=k<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
        elif arr[mid]<=arr[high]:
            if arr[mid]<=k<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1

if __name__ == "__main__":
    k = 8
    print(f"Array = {ARR}\nk = {k}")
    print(f"Index of {k} = {search_rotated_sorted(k=k)}")
