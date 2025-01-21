"""
1. Maximum consecutive ones
2. Find missing number
"""
from tkinter.constants import OFF

def maxcon_ones(arr=[1,0,1,1,0,1,1,1,1,1,0]):
    """
    TC=O(n)
    SC = O(1)
    """
    cur=0
    max=0
    for i in range(len(arr)):
        if arr[i]==1:
            cur+=1
            if cur>max:
                max=cur
        else:
            cur=0
    return max

print(maxcon_ones())


def find_miss_brute(arr=[5,3,1,6,2],n=6):
    """
    TC = O(n^2)
    SC = O(1)
    """
    for i in range(1,n+1):
        present=0
        for j in range(0,n-1):
            if i==arr[j]:
                present=1
                break
        if present==0: return i

print(find_miss_brute())

def find_miss_appr2(arr=[5,3,4,6,2],n=6):
    """
    This method is called hashing

    TC = O(2*n) = O(n)
    SC = O(n)
    """
    temp = [0]*(n+1)
    for el in arr:
        temp[el]=1
    for i in range(1,n+1):
        if temp[i]==0:
            return i

print(find_miss_appr2())

def find_miss_optimal(arr=[5,3,1,2,4],n=6):
    """
    TC = O(n)
    SC=O(1)

    Find the sum of first n numbers and subtract the sum of
    elements in the array. Make sure sum2 can store large values
    because if n=10^6 then sum2 ~= 10^12/2
    """
    sum2 = n*(n+1)/2
    sum1=0
    for el in arr:
        sum1+=el
    return int(sum2-sum1)
print(find_miss_optimal())


def find_miss_xor(arr=[5,3,1,4,2],n=6):
    """
    TC = O(n)
    SC = O(1)
    Using XOR we can find the missing element
    XOR1 = XOR(elements in the array)
    XOR2 = XOR(1 to n both included)
    ans = XOR(XOR1,XOR2)
    """
    XOR1 = 0
    XOR2 = 0
    for i in range(n-1):
        XOR1 = XOR1^arr[i]
        XOR2 = XOR2^(i+1)
    return XOR1^XOR2^n
print(find_miss_xor())
