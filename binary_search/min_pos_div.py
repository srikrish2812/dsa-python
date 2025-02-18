"""
Find the minimum positive divisor:
    You are provided with an array of integers 'arr' and an integer 'limit’. The task at hand is to identify the minimum positive integer divisor such that when each element in the given array 'arr' is divided by this 'divisor,' the sum of the resulting divisions does not surpass the specified 'limit.'

    Note: Consider the ceil value after every division calculation. For example, 9/2 = 5


"""
import math
ARR = [23,10,5,1,9,12]

def sum_div(arr, div):
    total = 0
    for num in arr:
        total += math.ceil(num/div)
    return total


def opt_appr(arr=ARR, lt=8):
    low=1
    high = max(arr)
    ans = max(arr)

    while low<=high:
        mid = low + (high-low)//2
        if sum_div(arr, mid)<=lt:
            ans =mid
            high=mid-1
        else:
            low =mid+1
    return ans
print(f"Using optimal approach = {opt_appr()}")
