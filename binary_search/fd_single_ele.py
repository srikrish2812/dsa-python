"""
Find the element that occurs just once in the  sorted array
"""
ARR = [2,2,4,4,6,6,7,9,9]
def brute_appr(arr=ARR):
    n = len(arr)
    if n==1: return arr[0]
    if arr[0]!=arr[1]: return arr[0]
    if arr[n-2]!=arr[n-1]: return arr[n-1]

    for i in range(1,n-1):
        if arr[i]!=arr[i-1] and arr[i]!=arr[i+1]:
            return arr[i]
    return -1

print(brute_appr())
