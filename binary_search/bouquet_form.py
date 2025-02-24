"""
Bouquet formation:

"""
def num_bouquets(arr,k,d):
    n = len(arr)
    count = 0
    bouquets= 0
    for i in range(n):
        if arr[i]<=d:
            count+=1
            if count==k:
                bouquets+=1
                count=0
        else:
            count = 0
    return bouquets

def brute_force(arr,k,m):
    """
    TC = O(n*(max-min+1))
    SC = O(1)
    """
    n = len(arr)
    if n<m*k: return -1
    for d in range(min(arr), max(arr)+1):
        if num_bouquets(arr,k,d)>=m:
            return d
    return -1

print(f"Using Brute Force approach: {brute_force(arr=[4,5,4,9,6,6,5,15,14],k=3,m=2)}")


def optimal_appr(arr,k,m):
    n = len(arr)
    low = min(arr)
    high = max(arr)
    ans = max(arr)
    if n<m*k: return -1

    while low<=high:
        mid = low + (high-low)//2
        if num_bouquets(arr,k,mid)>=m:
            ans =mid
            high=mid-1
        else:
            low = mid+1
    return ans

print(f"Using optimal approach: {optimal_appr([4,5,4,9,6,6,5,15,14],3,2)}")
