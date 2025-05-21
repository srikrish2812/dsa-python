"""
Binary Search:
    1. Initialize low = 0 and high = len(arr)-1
    2. Calculate mid = (low+high)//2
    3. Check if target == arr[mid]
    4. If target<arr[mid] then high=mid and low=low
    5. If target>arr[mid] then low=mid and high=high
    6. Repeat this until target==arr[mid]

TC = O(logn)
SC = O(1)
"""
ARR = [2,3,5,6,8,9,12,15]
def binary_search(arr=ARR,target=12):
    n = len(arr)
    low = 0
    high = n-1
    while low<=high:
        mid= (low+high)//2
        if target==arr[mid]:
            return mid
        elif target>arr[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1

print(binary_search())


def recursive_binary_search(arr, low, high, target):
    if low>high: return -1
    mid = (low+high)//2
    if target==arr[mid]: return mid
    elif target>arr[mid]: 
        return recursive_binary_search(arr,mid+1,high, target)
    else:
        return recursive_binary_search(arr, low, mid-1, target)
    
print(f"Recursive Binary Search: {recursive_binary_search(ARR,low=0,high=7,target=12)}")
