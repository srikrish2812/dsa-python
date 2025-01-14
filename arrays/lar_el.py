"""
1. Arrays have the same datatype and contiguous memory
2. Brute force approach is a very simple solution and is not efficient
3. Optimal approach is an efficient solution

Find the largest element in the array
"""

def brute_force(arr):
    # TC = O(nlogn)
    arr.sort()
    return arr[len(arr)-1]

def optimal(arr):
    # TC = O(n)
    max_el = arr[0]
    for el in arr[1:]:
        if el>max_el: max_el=el
    return max_el

a = [30,20,70,90,15]
print("Brute Force:",brute_force(a))
print("Optimal:",optimal(a))
