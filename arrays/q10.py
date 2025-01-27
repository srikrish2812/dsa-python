"""
Longest Subarray with Sum K
"""
ARR = [1,4,1,3,1,1,2,1,4]
K = 5
def brute_appr(arr=ARR, k=K):
    """
    TC = O(n^3)
    SC = O(1)
    """
    max=0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            sum=0
            for x in range(i,j+1):
                sum+=arr[x]
            if sum==k:
                length=j-i+1
                if length>max: max=length
    return max
print(brute_appr())
