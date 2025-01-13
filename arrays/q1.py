"""
Find max element in the array
"""
def brute_force(arr=[3,5,90,20,12]):
    """
    This approach has TC = O(nlogn) + O(n)
    """
    arr.sort()
    return arr[len(arr)-1]

print(brute_force())
