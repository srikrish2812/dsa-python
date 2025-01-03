"""
Bubble Sort:
    1. Push the maximum to the right by swapping adjacent elements
    2. Reduce the range from the left
    3. Repeat 1 and 2

Worst case TC = O(n^2)
Average case TC = O(n^2)
Best case(array is already sorted) TC = O(n)
"""

def bub_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1): # reduces the range from left
        is_sorted = True # breaks the loop if array is already sorted
        for j in range(0,i): # iterates the elements and compares them
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                is_sorted = False
        if is_sorted: break
    return arr

print(bub_sort(arr=[2,5,4,8,1]))
