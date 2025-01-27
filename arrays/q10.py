"""
Longest Subarray with Sum K
"""
ARR = [1,4,1,3,1,1,2,1,1,4]
K = 6
def brute_appr_1(arr=ARR, k=K):
    """
    TC = O(n^3)
    SC = O(1)
    """
    max=0
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            sum=0
            for x in range(i,j+1):
                sum+=arr[x]
            if sum==k:
                length=j-i+1
                if length>max: max=length
    return max
print(brute_appr_1())


def brute_appr_2(arr=ARR, k=K):
    """
    TC = O(n^2)
    SC = O(1)
    """
    max = 0
    n = len(arr)
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum += arr[j]
            length = j-i+1
            if sum==k:
                if length>max: max=length
    return max
print(brute_appr_2())


def prefix_sum_appr(arr=ARR, k=K):
    """
    We will use prefix sum appraoch to solve this.
    Use a map to store the cummulative sum and  its corresponding indec
    - update the prefix sum
    - check if sum==k then update max
    - check if sum-k is present in the dict() then update max
    - update prefic sum if it is not present in the dict() already

    1. Dictionary Lookup (sum - k in m):
    In Python, dictionary lookups are O(1) on average. However,
    in the worst case (due to hash collisions), they can degrade
    to O(n).
    2. Dictionary Insertion (m[sum] = i): Similarly, dictionary
    insertions are O(1) on average but can degrade to O(n) in the
    worst case.
    3. Average Case: Since dictionary operations are O(1) on average,
    the overall time complexity is O(n).
    4. Worst Case: In the worst case, where hash collisions cause
    dictionary operations to degrade to O(n), the overall time complexity
    is O(n^2)
    5. Space complexity = O(n)
    """
    sum, max = 0,0
    m = dict()
    n = len(arr)
    for i in range(n):
        sum+=arr[i]
        if sum==k:
            max = i+1
        if sum-k in m:
            length = i-m[sum-k]
            max = length if length>max else max

        if sum not in m:
            m[sum]=i
    return max

print(prefix_sum_appr())
