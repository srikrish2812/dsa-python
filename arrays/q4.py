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
