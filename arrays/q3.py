"""
1. Check if array is sorted
2. Remove duplicates
3. Move zeros to the end
"""

def is_sorted(arr):
    n = len(arr)
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            return False
    return True

arr_1 = [2,3,3,4,5,11]
arr_2 = [2,3,4,10,5,12]
print(f"Check if {arr_1} is sorted: {is_sorted(arr_1)}")
print(f"Check if {arr_2} is sorted: {is_sorted(arr_2)}")
