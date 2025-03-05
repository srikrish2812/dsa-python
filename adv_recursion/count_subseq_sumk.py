"""
Count the number of subsequences with sum==k
"""

def count_subseq(i,s,arr,n,k):
    """
    TC =O(2^n)
    SC = O(n) -> recursion stack space
    """
    if i>=n:
        if s==k:
            return 1
        return 0

    # pick
    s+=arr[i]
    left = count_subseq(i+1,s,arr,n,k)

    # not pick
    s-=arr[i]
    right = count_subseq(i+1,s,arr,n,k)

    return left + right


print("Count of subsequences with sum=k is", count_subseq(0,0,[3,4,7],3,7))
