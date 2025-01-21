"""
Intersection of two sorted arrays
"""

def brute_force(a=[2,3,3,3,4,4,5],b=[3,3,4,4,]):
    """
    m -> max(len(a),len(b))
    n -> min(len(a),len(b))
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


def optimal(a = [2,3,3,3,4,5],b=[3,3,4,4,]):
    """
    Two pointer approach

    TC = O(m+n)
    SC = O(min(m,n)) = O(n)
    """
    ans = []
    i,j=0,0
    while i<len(a) and j<len(b):
        if a[i]==b[j]:
            ans.append(a[i])
            i+=1
            j+=1
        elif a[i]<b[j]:
            i+=1
        else:
            j+=1
    return ans

print("Optimal Apprach =", optimal())


def get_intersect_three(a=[1,4,6,9],b=[4,6,7,10],c=[4,5,6,8]):
    ans =[]
    i,j,k=0,0,0
    while i<len(a) and j<len(b) and k<len(c):
        if a[i]==b[j] and b[j]==c[k] and c[k]==a[i]:
            ans.append(a[i])
            i+=1
            j+=1
            k+=1
        elif a[i]<b[j]:
            i+=1
        elif b[j]<c[k]:
            j+=1
        else:
            k+=1
    return ans

print("Optimal approach for intersection of 3 arrays",get_intersect_three())
