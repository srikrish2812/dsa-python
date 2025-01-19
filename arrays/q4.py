"""
Move zeros to the end
"""

def brute_force(arr):
    """
    1. Push non-zero elements to a new list
    2. place non-zero elements at the start of the array
    3. Make rest of the elements zero

    TC = O(n) iterates through the entire arr
    SC = O(n) creates a new list non_zero=[],
    it can have maximum of n non_zero elements
    """
    non_zero = []
    for el in arr:
        if el!=0:
            non_zero.append(el)
    for i in range(len(non_zero)):
        arr[i] = non_zero[i]
    for j in range(len(non_zero), len(arr)):
        arr[j] = 0
    print(arr)
    return arr

brute_force([0,0,3,0,0,5,0,0,7])


def optimal(arr):
    """
    Two Pointer approach:
        1. i will tell us where to place the non-zero element
        2. j will find the non-zero element
        3. i=0, j=0(even index 0 can have a non-zero element)

    TC = O(n) -> iterates over the entire array
    SC = O(n) -> no additional spaces created
    """
    i=0
    for j in range(0,len(arr)):
        if arr[j]!=0:
            arr[i], arr[j]=arr[j], arr[i]
            i+=1
    print(arr)
    return i+1 # number of non-zero elements
optimal(arr=[0,0,3,0,0,4,0,0,7])
