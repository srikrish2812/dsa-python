"""
Bubble Sort:
    1. Push the maximum to the right by swapping adjacent elements
    2. Reduce the range from the left
    3. Repeat 1 and 2
"""

def bub_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1): # reduces the range from left
        for j in range(0,i): # iterates the elements and compares them
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bub_sort(arr=[2,5,4,8,1]))
