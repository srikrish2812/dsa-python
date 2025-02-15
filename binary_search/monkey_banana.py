"""
Monkey/Koko Eating Bananas:

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours. Koko can decide her bananas-per-hour
eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that
pile. If the pile has less than k bananas, she eats all of them instead and will not eat any
more bananas during this hour. Koko likes to eat slowly but still wants to finish eating all
the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""
from math import ceil


ARR = [2,4,8,6]
H = 10
def brute_appr(arr=ARR, h=H):
    """
    1. The monkey will take n hours to finish the bananas with a given speed k>=max(arr) bananas/hours
    2. So minimum it takes n hours to eat the bananas
    3. So in the approach we will check for speeds from m=1 to max(arr)

    TC = O(n*max(arr))
    SC = O(1 )
    """
    n = len(arr)
    for m in range(1,max(arr)+1):
        total_time = 0
        for i in range(n):
            total_time+= ceil(arr[i]/m)
        if total_time<=h:
            return m
    return -1

print(f"Using brute force: {brute_appr()}")


def optimal_appr(arr=ARR,h=H):
    """
    TC = O(n* log(max(arr)))
    """
    low= 1
    high = max(arr)
    ans = max(arr)

    while low<=high:
        mid = low + (high-low)//2
        total_time = 0
        for ban in arr:
            total_time+= ceil(ban/mid)
        if total_time<=h:
            ans = mid
            high=mid-1
        else:
            low=mid+1
    return ans
print(f"Using Optimal Approach: {optimal_appr()}")
