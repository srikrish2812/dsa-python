"""
Intersection of two sorted arrays
"""

def brute_force(a=[2,3,3,3,4,4,5],b=[3,3,4,4,]):
    """
    m -> len(a)
    n -> len(b)
    TC = O(mn)
    SC = O(2n)
    """
    m = len(a)
    n = len(b)
    ans = []
    temp = [0]*n
    for i in range(m):
        for j in range(n):
            if a[i]==b[j] and temp[j]==0:
                ans.append(a[i])
                temp[j]=1
                break
            elif a[i]<b[j]:
                break
    return ans

print("Brute Force Approach =", brute_force())
