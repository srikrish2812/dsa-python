"""
Find the element that occurs only once in the array
"""

ARR=[7,4,5,9,6,5,4,9,7]
def brute_force(arr=ARR):
    n = len(arr)
    for i in range(n):
        count=0
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1
        if count==1:
            return arr[i]
print("Brute Force: Single element =", brute_force())


def better_1(arr=ARR):
    """
    TC = O(2n)
    SC = O(maxi+1)
    1. This approach is not good when the maximum element is too large.(~10^6)
    """
    n = len(arr)
    maxi = max(ARR)
    temp = [0]*(maxi+1)
    for i in range(n):
        temp[arr[i]]+=1
    for i in range(n):
        if temp[arr[i]]==1:
            return arr[i]

print("Better Approach-Hashing method :",better_1())

def dict_appr(arr=ARR):
    """
    TC = O(n+n)=O(n), both arr looping and dictionary have O(n) and O(n)
    SC = O(n), dictionary creation with max n key-value pairs
    """
    d = dict()
    for i in range(len(arr)):
        if arr[i] not in d.keys():
            d[arr[i]]=1
        else:
            d[arr[i]]+=1
    for key in d:
        if d[key]==1:
            return key
print("Dict Approach :",dict_appr())


def xor_approach(arr=ARR):
    xor = 0
    for num in arr:
        xor=xor^num
    return xor

print("XOR Approach", xor_approach())
