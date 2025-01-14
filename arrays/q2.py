"""
Find the second largest element
"""
# Brute force:
# sort first and then find the second largest
def appr_1(arr):
    # TC = O(nlogn) + O(n) [sorting+looping]
    # SC = O(n) [sorting additional space]
    n = len(arr)
    arr.sort()
    i = n-2
    while i>=0:
        if arr[i]!=arr[n-1]:
            return arr[i]
        i-=1
    return None

arr = [7,7,8,8,8,5,6]
print("Brute Force 1:", appr_1(arr))
