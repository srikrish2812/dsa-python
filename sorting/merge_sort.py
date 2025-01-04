"""
Merge Sort:
    1.Divide and merge is the main operation
    2.
    3.

Worst Case TC = O(nlogn)
"""

def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    k = 0
    n = right - left + 1
    new_arr = [0] * n

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            new_arr[k] = arr[i]
            i += 1
        else:
            new_arr[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        new_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        new_arr[k] = arr[j]
        j += 1
        k += 1

    for c in range(n):
        arr[left + c] = new_arr[c]

def merge_sort_helper(arr, left, right):
    if left == right:
        return
    mid = (left + right) // 2
    merge_sort_helper(arr, left, mid)
    merge_sort_helper(arr, mid + 1, right)
    merge(arr, left, mid, right)

def merge_sort(arr):
    n = len(arr)
    merge_sort_helper(arr,0,n-1)
    return arr


arr = [6,4,3,5,1,2]
print(merge_sort(arr))
print(*arr)
