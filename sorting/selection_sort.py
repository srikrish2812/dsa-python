"""
Selection sorting:
    1. Select the minimum
    2. Swap it with the first element in the current range
    3. Reduce the range/move the range to the right
"""
def sel_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]

    return arr

print(sel_sort(arr=[4,3,2,1]))
